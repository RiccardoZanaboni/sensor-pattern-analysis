import Time as t
import numpy as np
import ErrorLogger


class Room:
    """A class used to represent a room
        ...

        Attributes
        ------------------------
        name : str
            the name of the Room

        adjacencies : list of Room
            the Rooms near this one

        sensor : Sensor
            the Room's sensor

        Methods
        -----------------------

        alert_sensor(self, current_time, human)
            simulate the sensor's behaviour

        """

    def __init__(self, name, adjacencies, sensor, sensor_error_logger: ErrorLogger.ErrorLogger):
        """
        :param name: str
            the name of the Room
        :param adjacencies: list of Room
            the Rooms near this one
        :param sensor: Sensor
            the Room's sensor
        """
        self._sel = sensor_error_logger
        self.name = name
        self.adjacencies = adjacencies
        self.sensor = sensor

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def adjacencies(self):
        return self.__adjacencies

    @adjacencies.setter
    def adjacencies(self, adjacencies):
        self.__adjacencies = adjacencies

    @property
    def sensor(self):
        return self.__sensor

    @sensor.setter
    def sensor(self, sensor):
        self.__sensor = sensor

    def alert_sensor(self, current_time, human):
        """
        simulate the sensor's behaviour

        :param current_time: int
            current timer of the system
        :param human: Human
            person who lives in  the house
        :return:

        """

        if self.name == human.current_room.name:
            if self.sensor.state == 0:
                if np.random.uniform(0, 1) > self.sensor.prob_error:
                    self.sensor.state = 1
                    self.sensor.update_time_next_sample(current_time)
                    self.sensor.update(current_time)
                else:
                    self._sel.log_sensor_error(self.name, current_time)
            else:
                if t.Time.check_time_delta(current_time, self.sensor.time_next_sample):
                    self.sensor.update_time_next_sample(current_time)
        else:
            if self.sensor.state == 1 and self.sensor.time_next_sample <= current_time:
                self.sensor.state = 0
                self.sensor.update(current_time)

