#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 19:58:59 2017

@author: davi
"""
import numpy as np
import matplotlib.pyplot as plt

class Optimization():
   def set_function(self,function):
      """
      In: function def():
      """
      self.function = function
      
   def sphere(self,X):
      """
      In: numpy.array([x1,x2,...,xn])
      Out: float f(x1,x2,...,xn)
      """
      return np.sum(X**2)
   
   def venkataraman(self,X):
      """
      In: numpy.array([x1,x2,...,xn])
      Out: float f(x1,x2,...,xn)
      """
      return 3*(np.sin(0.5+0.25*X[0]*X[1]))*np.cos(X[0])
   
   def gradient(self,X):
      """
      In: numpy.array([x1,x2,...,xn])
      Out: numpy.array([dx1,dx2,...,dxn])
      """
      h = 1e-5
      derivative_array = np.empty(X.shape[0])
      for i in range(X.shape[0]):
         Xi = np.copy(X).astype(np.float)
         Xj = np.copy(X).astype(np.float)
         Xi[i]+=h
         Xj[i]-=h
         derivative_array[i] = (self.function(Xi)-self.function(Xj))/(2*h)
      return derivative_array
   
   def gradient_descent(self,X0,a,N):
      """
      In: numpy.array([x1_0,x2_0,...,xn_0]), float(learning_rate), int(iterations)
      Out: dict{'solution': [X_0,X_1,...,X_n], 'output': [f(X_0),f(X_1),...,f(X_n)]}
      """
      X = np.copy(X0)
      optimization_process = {'solution': [], 'output': []}
      for i in range(N):
         optimization_process['solution'].append(X)
         optimization_process['output'].append(self.function(X))
         X1 = X - a*self.gradient(X)
         X = np.copy(X1)
      return optimization_process

f = Optimization()
f.set_function(f.venkataraman)
X0 = np.array([.5,.5])
optimizer_log = f.gradient_descent(X0,.33,10)

"""
PLOTTTING
"""

x1 = np.linspace(-5, 5, 500)
x2 = np.linspace(-5, 5, 500)
x1, x2 = np.meshgrid(x1, x2)
X = np.array([x1,x2])
z = f.venkataraman(X)

plt.contour(x1,x2,z,np.arange(-3.3, 3.5, .5).tolist(), cmap='jet')

for i,solution in enumerate(optimizer_log['solution']):
   plt.scatter(solution[0],solution[1],c=[0,0,0],zorder=1000)
   plt.text(solution[0],solution[1],i,va='bottom',fontsize=8)

plt.savefig('gradient_descent.png')