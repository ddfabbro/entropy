#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:39:41 2017

@author: davi
"""
import numpy as np

np.seterr(divide='ignore', invalid='ignore')

def marginalEntropy(x,bins):
    np.seterr(divide='ignore', invalid='ignore')
    px = np.histogram(x,bins)[0]/float(np.sum(np.histogram(x,bins)[0]))
    return np.nansum(px*np.log(1/px))

def jointEntropy(x,y,bins):
    np.seterr(divide='ignore', invalid='ignore')
    pxy = np.histogram2d(x,y,bins)[0]/float(np.sum(np.histogram2d(x,y,bins)[0]))
    return np.nansum(pxy*np.log(1/pxy))

def mutualInformation(x,y,bins):
    np.seterr(divide='ignore', invalid='ignore')
    hx = marginalEntropy(x,bins)
    hy = marginalEntropy(y,bins)
    hxy = jointEntropy(x,y,bins)
    return hx+hy-hxy

def conditionalEntropy(x,y,bins):
    np.seterr(divide='ignore', invalid='ignore')
    hx = marginalEntropy(x,bins)
    hy = marginalEntropy(y,bins)
    hxy = jointEntropy(x,y,bins)
    return {'H(X|Y)': hxy-hy,
            'H(Y|X)': hxy-hx}