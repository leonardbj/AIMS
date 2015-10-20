""" Data, Estimation & Inference module

data_processing.py : open and process data to proper format

Author: Leonard Berrada
Date: 19 Oct 2015
"""

import pandas
import numpy as np
import copy
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(color_codes=True)


def process_from_file(filename,
                      plot_ts=False):
    """
    """

    my_dataframe = pandas.read_csv(filename)
#     my_dataframe.rename(columns={'Tide height (m)': 'y',
    my_dataframe.rename(columns={'Air temperature (C)': 'y',
                                 'True air temperature (C)': 'ytruth',
                                 'Reading Date and Time (ISO)': 't'},
                        inplace=True)

    my_dataframe['t'] = pandas.to_datetime(my_dataframe['t'])
    my_dataframe['t'] -= my_dataframe['t'].ix[0]
    my_dataframe['t'] = my_dataframe['t'].apply(
        lambda x: x / np.timedelta64(5, 'm'))

    print("data imported in dataframe")
    print('-' * 50)

    testing_indices = my_dataframe['y'].index[
        my_dataframe['y'].apply(np.isnan)]

    n_rows = len(my_dataframe.index)
    training_indices = [i for i in range(n_rows) if i not in testing_indices]

    training_df = my_dataframe[['t', 'y', 'ytruth']].ix[training_indices]
    testing_df = my_dataframe[['t', 'y', 'ytruth']].ix[testing_indices]

    print("training and testing dataframes created")
    print('-' * 50)

    print("Showing headers for verification:")
    print('\nTraining data :')
    print(training_df.head())
    print('\nTesting data :')
    print(testing_df.head())
    print('-' * 50)

    if plot_ts:
        training_df.plot()
        plt.show()

    return training_df, testing_df
