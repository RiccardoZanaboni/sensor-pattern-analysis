# class which attributes are meant for generate a random number from normal distribution
# @param seed is used to set numpy.random.seed
# @param mean and @param seed are the mean and standard deviation of the normal distribution respectively

import pandas as pd
import numpy as np
path = '/home/mattia/Documents/Tesi/data2/MovementState/'
file_name = 'mean_permanence.csv'


class MotionNormalDDP:

    def __init__(self, mu=0, std=0, seed=3):
        df = pd.read_csv(path + file_name, ',')

        self.seed = seed
        if mu != 0:
            self.mu = mu
        else:
            self.mu = float(df[df['Stat'] == 'mean']['Value'])
        if std != 0:
            self.std = std
        else:
            self.std = float(df[df['Stat'] == 'std']['Value'])

    @property
    def seed(self):
        return self.__seed

    @seed.setter
    def seed(self, seed):
        self.__seed = seed

    @property
    def mu(self):
        return self.__mu

    @mu.setter
    def mu(self, mu):
        self.__mu = mu

    @property
    def std(self):
        return self.__std

    @std.setter
    def std(self, std):
        self.__std = std

    def generate_waiting_time(self):
        np.random.seed(self.seed)
        rnd_number = int(np.random.normal(30, 2))

        return rnd_number

