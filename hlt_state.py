class HltState:

    WORKING = 100
    WARNING_NOT_SAMPLE = 50
    WARNING_EQUAL_MEASURES = 25
    NOT_WORKING = 0
    __possible_states = [WARNING_NOT_SAMPLE, WORKING, WARNING_EQUAL_MEASURES, NOT_WORKING]
    __sensor_sampling_times = {"hlt_4.csv": 600.607697501688, "hlt_7.csv": 600.577849117175,
                             "hlt_9.csv": 600.6786050895382,"hlt_11.csv": 600.6309148264984,
                             "hlt_19.csv": 600.6866297921038}

    def __init__(self, sensor_name):
        self.state = self.WORKING
        self.n_of_equals = 0
        self.st_mean = self.__sensor_sampling_times[sensor_name]
        self.timer = 0
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
    def timer(self):
        return self.__timer

    @timer.setter
    def timer(self, timer):
        self.__timer = timer

    @property
    def previous_sample(self):
        return self.__previous_sample

    @previous_sample.setter
    def previous_sample(self, previous_sample):
        self.__previous_sample = previous_sample

    def update_timer(self):
        self.timer += 60


if __name__ == "__main__":
    x = HltState()
    print(x.state)
