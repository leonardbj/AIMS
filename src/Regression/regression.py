""" Description here

Author: Leonard Berrada
Date: 4 Nov 2015
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class Regression:

    def __init__(self,
                 data=None,
                 **kwargs):
        
        assert data.has_key('ytrain')

        self._training_df = pd.DataFrame()

        self.n_training = len(data['ytrain'])
        self._training_df['y'] = data['ytrain']
        if data.has_key('xtrain'):
            self._training_df['x'] = data['xtrain']
        else:
            self._training_df['x'] = np.arange(self.n_training)

        if data.has_key('ytest'):
            self._testing_df = pd.DataFrame()
            self.n_testing = len(data['ytest'])
            self._testing_df['y'] = data['ytest']
            if data.has_key():
                self._testing_df['x'] = data['xtest']
            else:
                self._testing_df['x'] = np.arange(self.n_testing)

        print("done")
        print("-" * 50)
        print("showing headers for verification...")
        
        print("Training Data :")
        print(self._training_df.head())
        
        if hasattr(self, "n_testing"):
            print("Testing Data :")
            print(self._testing_df.head())

    def X_training(self,
                   indices=None,
                   start=None,
                   stop=None):

        if hasattr(indices, "__len__"):
            return self._training_df.x.values[indices]
        else:
            return self._training_df.x.values[start:stop]

    def X_testing(self,
                  indices=None,
                  start=None,
                  stop=None):

        if hasattr(indices, "__len__"):
            return self._testing_df.x.values[indices]
        else:
            return self._testing_df.x.values[start:stop]

    def Y_training(self,
                   indices=None,
                   start=None,
                   stop=None):

        if hasattr(indices, "__len__"):
            return self._training_df.y.values[indices]
        else:
            return self._training_df.y.values[start:stop]

    def Y_testing(self,
                  indices=None,
                  start=None,
                  stop=None):

        if hasattr(indices, "__len__"):
            return self._testing_df.y.values[indices]
        else:
            return self._testing_df.y.values[start:stop]

    def Y_pred(self,
               indices=None,
               start=None,
               stop=None):

        if hasattr(indices, "__len__"):
            return self._testing_df.ypred.values[indices]
        else:
            return self._testing_df.ypred.values[start:stop]

    def Y_error(self,
                indices=None,
                start=None,
                stop=None):

        if hasattr(indices, "__len__"):
            return self._testing_df.yerr.values[indices]
        else:
            return self._testing_df.yerr.values[start:stop]
        
    def embed_data(self):
        
        n = self.n_training - self.p
        self._emb_matrix = np.zeros((n, self.p))
        
        for k in range(self.p):
            self._emb_matrix[:, k] = self.Y_training(start=self.p - 1 - k,
                                                     stop=self.p - 1 - k + n)

    def fit(self):

        raise NotImplementedError("method should be overwritten")

    def predict(self, testing_data):

        raise NotImplementedError("method should be overwritten")

    def get(self, attr_name):

        return getattr(self, attr_name)

    def plot_attr(self, attr_name, show=False):

        attr_to_plot = getattr(self, attr_name)

        plt.plot(attr_to_plot)

        if show:
            plt.show()

    def plot_var(self, var_name, set_="", show=False):

        if 'train' in set_.lower():
            var_to_plot = self._training_df[var_name].values

        else:
            var_to_plot = self._testing_df[var_name].values

        plt.plot(var_to_plot)

        if show:
            plt.show()