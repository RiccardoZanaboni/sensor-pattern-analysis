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
    def __init__(self, df, df_hf, rooms):
        self.dataframe = df
        self.df_HF = df_hf
        self.rooms = rooms

    @property
    def dataframe(self):
        return self.__dataframe

    @dataframe.setter
    def dataframe(self, dataframe):
        self.__dataframe = dataframe

    @property
    def df_HF(self):
        return self.__df_HF

    @df_HF.setter
    def df_HF(self, dataframe):
        self.__df_HF = dataframe

    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, rooms):
        self.__rooms = rooms

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

    def update_df_HF(self, time, states):
        """
        storing the data for the histogram filter
        :param time: int
            the time of the misure
        :param states: int[]
            the state of sensor in the rooms
        :return:
        """
        dic = {"Time":'{:.4f}'.format(time)}
        for i in range(0, len(self.rooms)):
            dic[self.rooms[i]] = states[i]

        self.df_HF = self.df_HF.append(dic, ignore_index=True)
