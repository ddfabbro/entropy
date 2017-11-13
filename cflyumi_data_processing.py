#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 13:47:39 2017

@author: davi
"""
import numpy as np
import pandas
import matplotlib.pyplot as plt

def evaluate_profile(sample):
   """
   In: numpy.array()
   Out: int
   """
   gabarito = {'direcao': np.array([0,0,2,2,3,3,2,1,2,3,3,2]),
               'persuasao': np.array([2,2,1,0,2,0,1,0,1,1,1,0]),
               'apoio': np.array([1,1,0,1,0,1,0,2,0,0,0,1]),
               'delegacao': np.array([3,3,3,3,1,2,3,3,3,2,2,3])}
   
   return [len(sample[sample==gabarito['direcao']]),
           len(sample[sample==gabarito['persuasao']]),
           len(sample[sample==gabarito['apoio']]),
           len(sample[sample==gabarito['delegacao']])]

def evaluate_preference(sample):
   """
   In: numpy.array()
   Out: int
   """
   gabarito = {'10': 'medio','8': 'fraco','9': 'fraco', #14-1a, 14-1b,14-1c
               '4' : 'otimo','7': 'bom','6': 'medio', #14-2a, 14-2b, 14-2c
               '11': 'otimo','3': 'otimo','0': 'medio', #14-3a, 14-3b, 14-3c
               '5' : 'bom','2': 'otimo','1': 'otimo'} #14-4a, 14-4b, 14-4c
   
   return gabarito[str(sample)]

def evaluate_effectiveness(sample):
   """
   In: numpy.array()
   Out: int
   """
   gabarito = {'fraco': np.array([3,3,3,3,3,2,2,3,3,2,2,2]),
               'medio': np.array([1,1,2,1,2,1,1,2,2,0,3,0]),
               'bom': np.array([2,0,1,0,0,3,0,0,1,3,1,1]),
               'otimo': np.array([0,2,0,2,1,0,3,1,0,1,0,3])}
   
   return [len(sample[sample==gabarito['fraco']]),
           len(sample[sample==gabarito['medio']]),
           len(sample[sample==gabarito['bom']]),
           len(sample[sample==gabarito['otimo']])]

#Read data
raw_df = pandas.read_csv('data_tcc_cris.csv',encoding='utf-8')

#Remove unwanted columns
for i in range(4): del raw_df[raw_df.columns[0]]


#Split dataframe
info_df = raw_df.iloc[:,:8]
profile_df = raw_df.iloc[:,8:20]
preference_df = raw_df.iloc[:,21:25]
del raw_df

#Rename Columns
info_df.columns = ['idade','sexo','profissao','funcao','gestor','xp_estudo','xp_profissional','ferramentas']
profile_df.columns = ['q'+str(i+1) for i in range(12)]
preference_df.columns = ['q14-1','q14-2','q14-3','q14-4']

"""
"""
#Replace profile options by numbers
for i in range(profile_df.shape[1]):
   options = profile_df['q'+str(i+1)].unique()
   for j in range(len(options)):
      profile_df['q'+str(i+1)][profile_df['q'+str(i+1)]==options[j]] = j
del options

#get scores for each profile
profile_list = []
effectivensess_list = []
for i in range(profile_df.shape[0]):
   sample = np.array(profile_df.iloc[i,:].tolist())
   profile_list.append(evaluate_profile(sample))
   effectivensess_list.append(evaluate_effectiveness(sample))
profile_array = np.array(profile_list)
effectivensess_array = np.array(effectivensess_list)
profile_df = pandas.DataFrame({'direcao':profile_array[:,0],
                               'persusao':profile_array[:,1],
                               'apoio':profile_array[:,2],
                               'delegacao':profile_array[:,3],
                               'eficacia': (effectivensess_array[:,1]*1+effectivensess_array[:,1]*2+\
                                            effectivensess_array[:,2]*4+effectivensess_array[:,3]*8)/96.*100})
del sample, profile_list, profile_array, effectivensess_list, effectivensess_array

"""
"""
#Replace preference options by numbers
preference_df = preference_df['q14-1'].fillna('') + preference_df['q14-2'].fillna('') +\
                preference_df['q14-3'].fillna('') + preference_df['q14-4'].fillna('')
options = preference_df.unique()
for j in range(len(options)):
   preference_df[preference_df==options[j]] = j
del options

#get score for each preference
preference_list = []
for i in range(preference_df.shape[0]):
   sample = preference_df[i]
   preference_list.append(evaluate_preference(sample))
preference_array = np.array(preference_list)
preference_df = pandas.DataFrame({'pareto': preference_array})
del sample, preference_list, preference_array, i, j

#merge dataframes
df = pandas.concat([info_df, profile_df, preference_df], axis=1)
del info_df, profile_df, preference_df

#save to excel
writer = pandas.ExcelWriter('dados_tcc.xlsx')
df.to_excel(writer,'Sheet1')
writer.save()

