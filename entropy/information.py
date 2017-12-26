#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:39:41 2017

@author: davi
"""
import numpy as np

def marginalEntropy(x,bins):
    px = np.histogram(x,bins)[0]/float(np.sum(np.histogram(x,bins)[0]))
    return np.nansum(px*np.log(1/px))

def jointEntropy(x,y,bins):
    pxy = np.histogram2d(x,y,bins)[0]/float(np.sum(np.histogram2d(x,y,bins)[0]))
    return np.nansum(pxy*np.log(1/pxy))

def mutualInformation(x,y,bins):
    hx = marginalEntropy(x,bins)
    hy = marginalEntropy(y,bins)
    hxy = jointEntropy(x,y,bins)
    return hx+hy-hxy

def conditionalEntropy(x,y,bins):
    hx = marginalEntropy(x,bins)
    hy = marginalEntropy(y,bins)
    hxy = jointEntropy(x,y,bins)
    return {'H(X|Y)': hxy-hy,
            'H(Y|X)': hxy-hx}

if __name__ == "__main__":
    x = np.random.normal(0, 1, 1000)
    y = np.random.normal(0, 1, 1000)
    bins = 20
    
    print 'H(X) is ' + str(marginalEntropy(x,bins))
    print 'H(Y) is ' + str(marginalEntropy(y,bins))
    print 'H(X,Y) is ' + str(jointEntropy(x,y,bins))
    print 'I(X,Y) is ' + str(mutualInformation(x,y,bins))
    print 'H(X|Y) is ' + str(conditionalEntropy(x,y,bins)['H(X|Y)'])
    print 'H(Y|X) is ' + str(conditionalEntropy(x,y,bins)['H(Y|X)'])