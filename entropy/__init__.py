import numpy as np

np.seterr(divide='ignore', invalid='ignore')

def marginal_entropy(x,bins):
    px = np.histogram(x,bins)[0]/float(np.sum(np.histogram(x,bins)[0]))
    return np.nansum(px*np.log(1/px))

def joint_entropy(x,y,bins):
    pxy = np.histogram2d(x,y,bins)[0]/float(np.sum(np.histogram2d(x,y,bins)[0]))
    return np.nansum(pxy*np.log(1/pxy))

def mutual_information(x,y,bins):
    hx = marginal_entropy(x,bins)
    hy = marginal_entropy(y,bins)
    hxy = joint_entropy(x,y,bins)
    return hx+hy-hxy

def conditional_entropy(x,y,bins):
    hx = marginal_entropy(x,bins)
    hy = marginal_entropy(y,bins)
    hxy = joint_entropy(x,y,bins)
    return {'H(X|Y)': hxy-hy,
            'H(Y|X)': hxy-hx}
