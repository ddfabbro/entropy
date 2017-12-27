#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 20:00:45 2017

@author: davi
"""
import numpy as np
import sys; sys.path.append('../')
from entropy.information import *

x = np.random.normal(0, 1, 1000)
y = np.random.normal(0, 1, 1000)
bins = 20

print 'H(X) is ' + str(marginalEntropy(x,bins))
print 'H(Y) is ' + str(marginalEntropy(y,bins))
print 'H(X,Y) is ' + str(jointEntropy(x,y,bins))
print 'I(X,Y) is ' + str(mutualInformation(x,y,bins))
print 'H(X|Y) is ' + str(conditionalEntropy(x,y,bins)['H(X|Y)'])
print 'H(Y|X) is ' + str(conditionalEntropy(x,y,bins)['H(Y|X)'])
