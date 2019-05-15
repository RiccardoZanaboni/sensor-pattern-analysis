class Room:

    def __init__(self, name, adjacencies, sensor):
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

        if self.name == human.current_room.name:
            if self.sensor.state == 0:
                self.sensor.state = 1
                self.sensor.time_next_sample = self.sensor.max_timer + current_time
                self.sensor.update(current_time)
            else:
                if current_time == self.sensor.time_next_sample:
                    self.sensor.time_next_sample = self.sensor.max_timer + current_time
        else:
            if self.sensor.state == 1 and self.sensor.time_next_sample <= current_time:
                self.sensor.state = 0
                self.sensor.update(current_time)

