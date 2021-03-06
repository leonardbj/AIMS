""" Description here

Author: Leonard Berrada
Date: 5 Nov 2015
"""

import sys
sys.path.append("../")

import matplotlib.pyplot as plt

from Regression import AutoRegressive, AutoCorrelation, GaussianProcess, KalmanFilter

from process_data import data_from_file


file_name = "co2.mat"

data_dict = data_from_file(file_name)

# model = "GP"
model = "AR"
# model = "AC"
# model = "KF"


if model.lower() == 'kf':
    p = 25
    kf = KalmanFilter(data_dict, p)
    kf.fit()
    kf.display(out="./co2_kf.png")

if model.lower() == "ar":
    p = 50
    my_ar = AutoRegressive(data_dict, p)
    my_ar.fit()
    my_ar.predict()
    my_ar.display(out="./co2_ar.png")

if model.lower() == "ac":
    p = 50
    my_ac = AutoCorrelation(data_dict, p)
    my_ac.fit()
    my_ac.predict()
    my_ac.display(out="./co2_ac.png")
    my_ac.spectrum()


if model.lower() == "gp":

    Q = 3
    use_kernels = "exponential_quadratic* cosine"
    for _ in range(Q - 1):
        use_kernels += "+ exponential_quadratic * cosine"
#     use_kernels = 'rational_quadratic + periodic'
    use_means = "constant"
    estimator = "MLE"

    my_gp = GaussianProcess(data_dict=data_dict,
                            use_kernels=use_kernels,
                            use_means=use_means,
                            estimator=estimator,
                            sequential_mode=False)

    my_gp.predict()
    my_gp.compute_score()
    my_gp.show_prediction(out="./co2_gp.png")
