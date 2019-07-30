
class Sensor:
    """A class used to represent the motion sensor and how it works
                ...

                Attributes
                ------------------------
                state : int
                    represents the value of the measure of the sensor(1 = isMoving, 0 = notMoving)

                gateway : Gateway
                    where the measures are sent to

                time_next_sample : int
                    when the future sample will be

                name : str
                    represents the room where the sensor is
                Methods

                sleep_time : int
                    the sensor doesn't sample after an "isMoving" for this time
                -----------------------

                update(self, current_time)
                    simulate the sending of data to the gateway

                """

    def __init__(self, name,  gateway, sleep_time, prob_error):
        self.state = 0
        self.gateway = gateway
        self.time_next_sample = 0
        self.name = name
        self.sleep_time = sleep_time
        self.prob_error = prob_error

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

    @property
    def sleep_time(self):
        return self.__sleep_time

    @sleep_time.setter
    def sleep_time(self, sleep_time):
        self.__sleep_time = sleep_time

    @property
    def prob_error(self):
        return self.__prob_error

    @prob_error.setter
    def prob_error(self, prob_error):
        self.__prob_error = prob_error

    def update_time_next_sample(self, current_time):
        self.time_next_sample = current_time + self.sleep_time

    def update(self, current_time):
        """
        simulate the sending of data to the gateway (writing in csv)
        :param current_time: int
            the timer of the system
        :return:
        """
        self.gateway.update_dataframe(current_time, self.name, self.state)
