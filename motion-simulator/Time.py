import math


class Time:
    """A class used to manage the system clock
        ...

        Attributes
        ------------------------
        START_TIME  : float
            time when simulation starts

        STOP_TIME  : float
            time when simulation ends

        epsilon : float
            this value represents the precision of floats comparison

        delta : float
            quantum of time by which the system time is updated

        current_time : float
            the current time of the system

        Methods
            -----------------------

        increase_time(current_date)
                   increase timer(@param current_date) by delta seconds

        check_time_delta(a, b)
            compare the absolute difference between two float to a threshold epsilon
    """
    epsilon = 0
    def __init__(self, start_time, stop_time, epsilon, delta):

        self.START_TIME = start_time
        self.STOP_TIME = stop_time
        Time.epsilon = epsilon
        self.delta = delta
        self.current_time = self.START_TIME


    @property
    def delta(self):
        return self.__delta

    @delta.setter
    def delta(self, delta):
        self.__delta = delta

    @property
    def current_time(self):
        return self.__current_time

    @current_time.setter
    def current_time(self,current_time):
        self.__current_time = current_time

    def increase_time(self):
        """ increase timer(@param current_date) by delta seconds """
        self.current_time = self.current_time + self.delta

    @staticmethod
    def check_time_delta(a, b):
        """ compare the absolute difference between two float to a threshold epsilon """
        if abs(a-b) < Time.epsilon:
            return True
        return False

    @staticmethod
    def truncate(number, digits) -> float:
        stepper = 10.0 ** digits
        return math.trunc(stepper * number) / stepper
