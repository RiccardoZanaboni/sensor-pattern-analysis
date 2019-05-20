
import numpy as np


class NormalDDP:
    """A class used to express the Normal ddp on which  it's decided the time of permanence in a room
            ...

            Attributes
            ------------------------
            mu :  int
                the mean of the Normal ddp
            std : int
                the standard deviation of   the Normal ddp

            seed : int
                used to set numpy.random.seed
            Methods
            -----------------------

            generate_waiting_time(self)
                generate randomly the time of permanence in the room

    """

    def __init__(self, mu, std, seed):

        self.mu = mu
        self.std = std
        self.seed = seed

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

    def generate_random_time(self):
        """
        generate randomly the time of permanence in the room :
        using numpy.random.normal() and the attributes of the class which are used to set
        this function parameters

        :return: int
            the randomly generated waiting time
        """
        #  np.random.seed(self.seed)                                # test mode only!
        rnd_number = int(np.random.normal(self.mu, self.std))

        return rnd_number

