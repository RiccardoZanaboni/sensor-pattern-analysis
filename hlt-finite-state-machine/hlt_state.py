import Read_configurations


class HltState:
    """
    Class which represents the state of the final state machine of the sensor

    Attributes
    ------------------------
    state : int
        the state of the final state machine
    n_of_equals : int
        number of equals measures
    st_mean : float
        mean of sampling time of selected sensor
    timer : int
        time pf the system
    previous_sample : [] int
        the last three samples, initialised to a default value

    Methods
    -----------------------
    update_timer :
    update the timer of the sensor (1 minute)

    """

    possible_states = Read_configurations.open_json()["FSM_info"]["state_values"]
    state = list(possible_states.values())

    def __init__(self):
        self.state = self.state[0]
        self.n_of_equals = 0
        self.st_mean = Read_configurations.open_json()["FSM_info"]["sampling_mean"]
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

