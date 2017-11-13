import numpy as np

def information_xy(x,y,bins):
   """
   Calculates:
   ---Marginal Entropy H(x)
   ---Marginal Entropy H(y)
   ---Joint Entropy H(x,y)
   ---Mutual Information I(x,y)
   ---Conditional Entropy H(X|Y)
   ---Conditional Entropy H(Y|X)
   
   In: numpy.array (1D), numpy.array(1D), int
   Out: (float, float, ... , float) 
   """
   px = np.histogram(x,bins)[0]/float(np.sum(np.histogram(x,bins)[0]))
   py = np.histogram(y,bins)[0]/float(np.sum(np.histogram(y,bins)[0]))
   pxy = np.histogram2d(x,y,bins)[0]/float(np.sum(np.histogram2d(x,y,bins)[0]))
   
   hx = np.nansum(px*np.log(1/px))
   hy = np.nansum(py*np.log(1/py))
   hxy = np.nansum(pxy*np.log(1/pxy))
   ixy =  hy+hx-hxy
   hx_y = hxy-hy
   hy_x = hxy-hx
   
   return (hx,hy,hxy,ixy,hx_y,hy_x)