""" Data, Estimation & Inference module

main.py : execution script

Author: Leonard Berrada
Date: 19 Oct 2015
"""

from data_processing import process_from_file
from GP_model import predict
from tune import optimize_hyperparameters
from utils import timeit
import csv

@timeit
def run(filename=None,
        variable=None,
        use_kernels=None,
        use_means=None,
        estimator=None,
        sequential_mode=None):
    
    print(variable, use_means, use_kernels, estimator)

    Xtraining, Ytraining, Xtesting, Ytestingtruth, t0 = process_from_file(filename,
                                                                          variable=variable)
    
    params = optimize_hyperparameters(Xtraining,
                                      Ytraining,
                                      use_kernels=use_kernels,
                                      use_means=use_means,
                                      estimator=estimator,
                                      variable=variable)
    
#     params = [0.1401, 3.0305, 214.6188, 149.9601, 11.6825]
#     predict(Xtraining=Xtraining,
#             Ytraining=Ytraining,
#             Xtesting=Xtesting,
#             params=params,
#             Ytestingtruth=Ytestingtruth,
#             use_kernels=use_kernels,
#             use_means=use_means,
#             sequential_mode=sequential_mode,
#             estimator=estimator,
#             variable=variable,
#             t0=t0,
#             show_plot=False)
    

filename = 'sotonmet.txt'
variable = 'temperature'
use_kernels = "matern_12 + periodic"
use_means = "constant"
estimator = "MAP"
sequential_mode = False

for estimator in ["MLE", "MAP"]:
    for variable in ["tide", "temperature"]:
        for op in ["+", "*"]:
            for use_kernels in ["exponential_quadratic" + op + "exponential_quadratic_2", 
                                "exponential_quadratic" + op + "periodic", 
                                "rational_quadratic" + op + "periodic",
                                "matern_12" + op + "periodic",
                                "matern_32" + op + "periodic"]:
                for use_means in ["constant", "constant + periodic"]:
                    try:
                        run(filename=filename,
                            variable=variable,
                            use_kernels=use_kernels,
                            estimator=estimator,
                            use_means=use_means,
                            sequential_mode=sequential_mode)
                    except:
                        print("damn")
                        with open("./out/results.csv", 'a', newline='') as csvfile:
                            my_writer = csv.writer(csvfile, delimiter='\t',
                                                   quoting=csv.QUOTE_MINIMAL)
                            my_writer.writerow(["shit happened with following parameters:", 
                                                 variable,
                                                 use_kernels,
                                                 use_means,
                                                 estimator])




# run(filename=filename,
#     variable=variable,
#     use_kernels=use_kernels,
#     estimator=estimator,
#     use_means=use_means,
#     sequential_mode=sequential_mode)
        






