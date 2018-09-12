# entropy
A minimal Python module that calculates information metrics according to Shannon's information theory \[1\].

## Installation

There is no installation for this package.

To use it, simply clone this repository by

```
git clone https://github.com/ddfabbro/entropy.git
```

and add the root directory to your `PYTHONPATH` environment variable

```
export PYTHONPATH=$PYTHONPATH:$(pwd)/entropy
```

## Usage

```
>>> import numpy as np
>>> from entropy import *
>>> x = np.random.normal(0, 1, 1000)
>>> y = np.random.normal(0, 1, 1000)
>>> bins = 20
>>> print('H(X) is {}'.format(marginal_entropy(x,bins)))
H(X) is 2.498960151390878
>>> print('H(Y) is {}'.format(marginal_entropy(y,bins)))
H(Y) is 2.565558730095208
>>> print('H(X,Y) is {}'.format(joint_entropy(x,y,bins)))
H(X,Y) is 4.906705770038114
>>> print('I(X,Y) is {}'.format(mutual_information(x,y,bins)))
I(X,Y) is 0.15781311144797172
>>> print('H(X|Y) is {}'.format(conditional_entropy(x,y,bins)['H(X|Y)']))
H(X|Y) is 2.3411470399429057
>>> print('H(Y|X) is {}'.format(conditional_entropy(x,y,bins)['H(Y|X)']))
H(Y|X) is 2.407745618647236
```

## References

1. Shannon, Claude E. "A mathematical theory of communication." _ACM SIGMOBILE Mobile Computing and Communications Review_ 5.1 (2001): 3-55.
