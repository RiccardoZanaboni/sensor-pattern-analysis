import AbstractDDP
import numpy as np


class NormalDDP(AbstractDDP.AbstractDDP):
    """A class used to express the Normal ddp on which  it's decided the time of permanence in a room
            ...

            Attributes
            ------------------------

            Methods
            -----------------------

            generate_random_time(self)
                generate randomly from  normal ddp the time of permanence in the room

    """

    def __init__(self, mu, std, seed, test_mode):
        super().__init__(mu, std, seed, test_mode)

    def generate_random_time(self):
        """
        generate randomly the time of permanence in the room :
        using numpy.random.normal() and the attributes of the super class which are used to set
        this function parameters

        :return: int
            the randomly generated waiting time
        """
        if self.test_mode == "on":
            np.random.seed(self.seed)

        rnd_number = np.random.normal(super().mu, super().std)
        rnd_number = round(rnd_number, 1)

        return rnd_number

