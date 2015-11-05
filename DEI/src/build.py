""" Description here

Author: Leonard Berrada
Date: 22 Oct 2015
"""

import numpy as np

from kernels import get_kernel
from means import get_mean
import copy

def train_on(self,
             X1=None,
             X2=None,
             XX=None,
             Xtesting=None):
    
    if hasattr(XX, "__len__"):
        X1 = XX[:, None]
        X2 = XX[None, :]
    
    # clean string for combination of means and kernels
    use_means = self.use_means.replace(" ", "")
    use_kernels = self.use_kernels.replace(" ", "")
    
    # ensure aux_params has the right data structure
    aux_params = copy.copy(self.params)
    aux_params = list(aux_params)
    
    #===========================================================================
    # Compute covariance matrix (muK)
    #===========================================================================
    
    sigma_n = aux_params.pop(0)
    
    # parse string
    temp_str = use_kernels.replace("*", "+")
    all_kernels = temp_str.split("+")

    use_kernels = use_kernels[len(all_kernels[0]):]
    K = get_kernel(all_kernels.pop(0))(X1=X1,
                                       X2=X2,
                                       params=aux_params)

    while len(all_kernels):
        op = use_kernels[0]
        use_kernels = use_kernels[len(all_kernels[0]) + 1:]
        if op == "+":
            K += get_kernel(all_kernels.pop(0))(X1=X1,
                                                X2=X2,
                                                params=aux_params)
        
        elif op == "*":
            K *= get_kernel(all_kernels.pop(0))(X1=X1,
                                                X2=X2,
                                                params=aux_params)
        else:
            raise ValueError("shit happened : %s" % op)
    
    if not hasattr(K, "__len__"):
        K += sigma_n ** 2
         
    elif len(K.shape) == 2 and K.shape[0] == K.shape[1]:
        n = len(K)
        same_x = [np.arange(n), np.arange(n)]
        K[same_x] += sigma_n ** 2
        
        
    mu = 0
    
    # if no testing data, no need to compute mean
    if not hasattr(Xtesting, "__len__") and Xtesting == None:
        return mu, K  
        
    #===========================================================================
    # Compute mean (mu)
    #===========================================================================
    
    temp_str = use_means.replace("*", "+")
    all_means = temp_str.split("+")
    
    use_means = use_means[len(all_means[0]):]
    mu = get_mean(all_means.pop(0))(Xtesting=Xtesting,
                                    params=aux_params)
    
    while len(all_kernels):
        op = use_means[0]
        use_means = use_means[len(all_means[0]) + 1:]
        if op == "+":
            mu += get_mean(all_means.pop(0))(Xtesting=Xtesting,
                                             params=aux_params)
        
        elif op == "*":
            mu *= get_mean(all_means.pop(0))(Xtesting=Xtesting,
                                             params=aux_params)
        else:
            raise ValueError("shit happened : %s" % op)
        
    return mu, K
