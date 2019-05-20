class Gateway:
    """A class used to represent the gateway
            ...

            Attributes
            ------------------------
            dataframe :  pandas.DataFrame
                    used to store the sensors' data
            Methods
            -----------------------

            update_dataframe(self, time, room, state)
                    simulate the storing of data

     """
    def __init__(self, df):
        self.dataframe = df

    @property
    def dataframe(self):
        return self.__dataframe

    @dataframe.setter
    def dataframe(self, dataframe):
        self.__dataframe = dataframe

    def update_dataframe(self, time, room, state):
        """
        simulate the storing of data
        :param time: int
            the time of the measure
        :param room: str
            where the sensor is
        :param state: int
            the value of the measure
        :return:
        """
        self.dataframe = self.dataframe.append({'Time': time, 'Room': room, 'State': state}, ignore_index=True)
