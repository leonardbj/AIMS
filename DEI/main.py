""" Data, Estimation & Inference module

main.py : execution script

Author: Leonard Berrada
Date: 19 Oct 2015
"""

from data_processing import process_from_file
from kernels import gaussian_kernel

filename = 'sotonmet.txt'

training_df, testing_df = process_from_file(filename)
X = training_df.t.values
Y = training_df.y.values
Xstar = testing_df.t.values

sigma_f = 1.
sigma_n = 1.
l = 0.1

y_mean, y_var = gaussian_kernel(X=X, 
                                Y=Y, 
                                xstar=Xstar, 
                                sigma_f=sigma_f, 
                                sigma_n=sigma_n, 
                                l=l)






