from abc import ABC,abstractmethod


class AbstractDDP(ABC):
    """An abstract class used to express the ddp on which  it's decided the time of permanence in a room.
       The subclasses must will define the type of the ddp function
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

                generate_random_time(self)
                    generate randomly the time of permanence in the room

        """

    def __init__(self, mu, std, seed, test_mode):
        super().__init__()
        self.mu = mu
        self.std = std
        self.seed = seed
        self.test_mode = test_mode

    @abstractmethod
    def generate_random_time(self):
        pass

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

    @property
    def test_mode(self):
        return self.__test_mode

    @test_mode.setter
    def test_mode(self, test_mode):
        self.__test_mode = test_mode
