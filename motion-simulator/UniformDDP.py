import numpy as np
import time


class UniformDDp:
    """A class used to express the Uniform ddp on which  it's decided the time of permanence in a room.
        Human can have an arbitrary number of ddp function to base his decision on
            ...

            Attributes
            ------------------------
            lower : int
                it is the lower bound of the domain of the uniform function
            upper : int
                it is the highest bound  of the domain of the function

            Methods
            -----------------------

            generate_random_time(self)
                generate randomly from  uniform ddp the time of permanence in the room

    """

    def __init__(self, lower, upper, seed, test_mode):
        self.lower = lower
        self.upper = upper
        self.test_mode = test_mode

        if self.test_mode == "on":
            self.seed = seed
        else:
            self.seed = int(time.time())  #time.time mi da il tempo corrente in secondi

        np.random.seed(self.seed)  # makes the random numbers predictable

    @property
    def seed(self):
        return self.__seed

    @seed.setter
    def seed(self, seed):
        self.__seed = seed

    @property
    def test_mode(self):
        return self.__test_mode

    @test_mode.setter
    def test_mode(self, test_mode):
        self.__test_mode = test_mode

    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower):
        self.__lower = lower

    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper):
        self.__upper = upper

    def generate_random_time(self):
        """
            generate randomly the time of permanence in the room :
            using numpy.random.normal() and the attributes of the super class which are used to set
            this function parameters

            :return: int
                the randomly generated waiting time
        """

        random_time = np.random.uniform(self.lower, self.upper)
        return int(random_time)
