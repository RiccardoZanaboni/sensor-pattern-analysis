
class Sensor:

    def __init__(self, name, max_timer, gateway):
        self.state = 0
        self.gateway = gateway
        self.max_timer = max_timer
        self.time_next_sample = 0
        self.name = name

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state

    @property
    def gateway(self):
        return self.__gateway

    @gateway.setter
    def gateway(self, gateway):
        self.__gateway = gateway

    @property
    def max_timer(self):
        return self.__max_timer

    @max_timer.setter
    def max_timer(self, max_timer):
        self.__max_timer = max_timer

    @property
    def time_next_sample(self):
        return self.__time_next_sample

    @time_next_sample.setter
    def time_next_sample(self, time_next_sample):
        self.__time_next_sample = time_next_sample

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def update(self, current_time):
        self.gateway.update_dataframe(current_time, self.name, self.state)
