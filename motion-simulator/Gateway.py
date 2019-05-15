class Gateway:

    def __init__(self,df):
        self.dataframe = df

    @property
    def dataframe(self):
        return self.__dataframe

    @dataframe.setter
    def dataframe(self, dataframe):
        self.__dataframe = dataframe

    def update_dataframe(self, time, room, state):
        self.dataframe = self.dataframe.append({'Time': time, 'Room': room, 'State': state}, ignore_index=True)
