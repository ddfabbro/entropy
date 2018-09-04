import numpy as np
from entropy import *

x = np.random.normal(0, 1, 1000)
y = np.random.normal(0, 1, 1000)
bins = 20

print('H(X) is ' + str(marginal_entropy(x,bins)))
print('H(Y) is ' + str(marginal_entropy(y,bins)))
print('H(X,Y) is ' + str(joint_entropy(x,y,bins)))
print('I(X,Y) is ' + str(mutual_information(x,y,bins)))
print('H(X|Y) is ' + str(conditional_entropy(x,y,bins)['H(X|Y)']))
print('H(Y|X) is ' + str(conditional_entropy(x,y,bins)['H(Y|X)']))
