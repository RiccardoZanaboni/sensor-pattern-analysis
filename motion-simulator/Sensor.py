
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

                model : NormalDDP
                    the DDP on which the randomly error for the sample time  is generated
                -----------------------

                update(self, current_time)
                    simulate the sending of data to the gateway

                """

    def __init__(self, name,  gateway, model):
        self.state = 0
        self.gateway = gateway
        self.time_next_sample = 0
        self.name = name
        self.sample_time_error = model

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
    def sample_time_error(self):
        return self.__sample_time_error

    @sample_time_error.setter
    def sample_time_error(self, error):
        self.__sample_time_error = error

    def update_time_next_sample(self, current_time):
        tmp = self.sample_time_error.generate_random_time()
        self.time_next_sample = current_time + tmp

    def update(self, current_time):
        """
        simulate the sending of data to the gateway (writing in csv)
        :param current_time: int
            the timer of the system
        :return:
        """
        self.gateway.update_dataframe(current_time, self.name, self.state)
