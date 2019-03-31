class HltState:

    WORKING = 100
    WARNING_NOT_SAMPLE = 50
    WARNING_EQUAL_MEASURES = 25
    NOT_WORKING = 0
    __possible_states = [WARNING_NOT_SAMPLE, WORKING, WARNING_EQUAL_MEASURES, NOT_WORKING]

    def __init__(self):
        self.state = self.WORKING
        self.n_of_equals = 0
        self.n_missing = 0
        self.previous_sample = [-1, -1, -1]

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        if state in self.__possible_states:
            self.__state = state
        else:
            self.__state = -1

    @property
    def n_of_equals(self):
        return self.__n_of_equals

    @n_of_equals.setter
    def n_of_equals(self, n_of_equals):
        self.__n_of_equals = n_of_equals

    @property
    def n_missing(self):
        return self.__n_missing

    @n_missing.setter
    def n_missing(self, n_missing):
        self.__n_missing = n_missing

    @property
    def previous_sample(self):
        return self.__previous_sample

    @previous_sample.setter
    def previous_sample(self, previous_sample):
        self.__previous_sample = previous_sample


if __name__ == "__main__":
    x = HltState()
    print(x.state)
