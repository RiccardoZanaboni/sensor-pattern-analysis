import numpy as np


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

    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

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
        # np.random.seed(self.seed)
        random_time = np.random.uniform(self.lower, self.upper)
        return int(random_time)
