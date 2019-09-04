class Belief:
    """
    Class which apply the Bayes Filter Algorithm
     Attributes
     ------------------------
     bel : float []
        probability distribution over all possible states, conditioned by the observations so far
        bel(xt):=P(xt∣e1:t)
     bel_projected : float []
        probability distribution over all the possible states at time t, given only past observations
        bel⎯projected(xt):=P(xt∣e1:t−1)
     pos : String []
        state domain
     prob_state : list(float [])
        list of probabilities to go in a room given the current room
     sensors_error_rate : list(float [])
        list of probabilities to be in a room given the sensors' measures
     Methods
     -----------------------
     bel_upgrade(self, sensor_output)
    """

    def __init__(self, bel, pos, prob_state, ser):
        self.bel = bel
        self.bel_projected = [0 for x in range(0, len(pos))]
        self.pos = pos
        self.prob_state = prob_state
        self.sensors_error_rate = ser

    @property
    def bel(self):
        return self.__bel

    @bel.setter
    def bel(self, bel):
        self.__bel = bel

    @property
    def bel_projected(self):
        return self.__bel_projected

    @bel_projected.setter
    def bel_projected(self, bel_projected):
        self.__bel_projected = bel_projected

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, pos):
        self.__pos = pos

    @property
    def prob_state(self):
        return self.__prob_state

    @prob_state.setter
    def prob_state(self, prob_state):
        self.__prob_state = prob_state

    @property
    def sensors_error_rate(self):
        return self.__sensors_error_rate

    @sensors_error_rate.setter
    def sensors_error_rate(self, sensors_error_rate):
        self.__sensors_error_rate = sensors_error_rate

    def bel_upgrade(self, sensor_output, transactions):
        for i in range(0, len(transactions)):
            if transactions[i] != 0:
                self.bel = [y * x for y, x in zip(self.bel_projected, self.sensors_error_rate[i][sensor_output[i]])]
        eta = 1/sum(self.bel)
        self.bel = [x * eta for x in self.bel]

    def bel_projected_upgrade(self):
        for i in range(0, len(self.pos)):
            self.bel_projected[i] = [x * self.bel[i] for x in self.prob_state[i]]
        self.bel_projected = [sum(x) for x in zip(*self.bel_projected)]