#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 13:47:10 2017

@author: davi
"""

import numpy as np 
import random
from gradient_descent import MathFunction
 
class EvolutionaryAlgorithm():
    
   def __init__(self,signal,fitness,population_size,variables,bounds):
      if signal == 'max':
         self.signal = 1
      else:
         self.signal = -1
      self.fitness = fitness
      self.population_size = population_size
      self.variables = variables
      self.lower_bound = bounds[0]
      self.upper_bound = bounds[1]
   
   def new_individual(self):
      return np.random.uniform(self.lower_bound,self.upper_bound,self.variables)

   def new_population(self):
      return np.array([self.new_individual() for x in range(self.population_size)])
   
   def crossover(self,parents):
      return np.mean(parents,0)

   def mutation(self,offspring):
      return np.clip(np.random.uniform(.8,1.2)*offspring,self.lower_bound,self.upper_bound)
   
   def roulette(self,population):
      try:
         self.population_fitness_
      except:
         self.population_fitness_ = self.population_fitness(population)
      if np.min(self.population_fitness_) < 0: 
         normalized_fitness = self.population_fitness_ + abs(np.min(self.population_fitness_))
      else:
         normalized_fitness = self.population_fitness_ - abs(np.min(self.population_fitness_))
   
      roulette_ = np.cumsum(normalized_fitness/float(np.sum(normalized_fitness)))
      pocket = np.random.rand()
      for arrow, fitness in enumerate(roulette_):
         if pocket <= fitness:
            return population[arrow]
   
   def population_fitness(self,population):
      return np.array([self.signal*self.fitness(X) for X in population])
   
   def best(self,population):
      try:
         self.population_fitness_
      except:
         self.population_fitness_ = self.population_fitness(population)
      return population[np.where(self.population_fitness_==np.max(self.population_fitness_))][0]

   def evolve(self,p_crossover,p_mutation,iterations):
      optimization_process = {'solutions': [], 'output': []}
      population = self.new_population()
      
      for generations in range(iterations):
         self.population_fitness_ = self.population_fitness(population)
         optimization_process['solutions'].append(population)
         optimization_process['output'].append(self.signal*self.population_fitness_)
         
         parents_list = []
         
         #Elitism
         parents_list.append(self.best(population))
         
         #Crossover
         while len(parents_list) < self.population_size:
            parents = np.array([self.roulette(population),
                                self.roulette(population)])
            if np.random.rand() < p_crossover:
               offspring = self.crossover(parents)
               parents_list.append(offspring)
            else:
               parents_list.append(random.choice(parents))
         
         #Mutation
         for individual in parents_list:
            if np.random.rand() < p_mutation :
               individual = self.mutation(individual)
         
         population = np.array(parents_list)
            
      return optimization_process
   
if __name__ == "__main__":   
   
   function = MathFunction()
   ecosystem = EvolutionaryAlgorithm('max',function.venkataraman,20,2,[-5,5])
   optimizer_results =ecosystem.evolve(.8,.3,10)
   
   """
   population = ecosystem.new_population()
   population_fitness = ecosystem.population_fitness(population)
   best = ecosystem.best(population)
   parents = np.array([ecosystem.roulette(population),ecosystem.roulette(population)])
   offspring = ecosystem.crossover(parents)
   """