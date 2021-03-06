""" Description here

Author: Leonard Berrada
Date: 2 Nov 2015
"""

import sys
sys.path.append("../")

try:
    import seaborn as sns
    sns.set(color_codes=True)
except:
    pass

from process_data import data_from_file

from Regression import AutoRegressive, AutoCorrelation

# file_name = "finPredProb.mat"
# file_name = "co2.mat"
# file_name = "sunspots.mat"
# file_name = "mg.mat"
file_name = "fXSamples.mat"

ix = 1
p = 5

args = data_from_file(file_name,
                      ix=ix)

my_ar = AutoRegressive(*args, p=p)
my_ar.fit()
my_ar.predict()
# my_ar.plot_var('ypred')
 
my_ac = AutoCorrelation(*args, p=p)
my_ac.fit()
my_ac.predict()
# my_ac.plot_var('ypred', show=True)
 
my_ac.spectrum()
my_ac.plot_attr('spectrum', show=True)


