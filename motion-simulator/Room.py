class Room:

    def __init__(self, name, adjacencies):
        self.name = name
        self.adjacencies = adjacencies
        self.sensor = 0


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


