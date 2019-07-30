import pandas as pd


class ReadFile:
    """
        Class which read from a csv file(@param file_name) and create a Pandas.DataFrame

         Attributes
         ------------------------
         file_name : str
            name of the csv file from which the Pandas.DataFrame is created

         df : Pandas.DataFrame
            Pandas.DataFrame which contains the MovementState sensors's output


        """

    def __init__(self, file_name):
        self.file_name = file_name
        self.df = pd.read_csv(self.file_name, ',')

    @property
    def df(self):
        return self.__df

    @df.setter
    def df(self, df):
        self.__df = df

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, filename):
        self.__filename = filename


if __name__ == '__main__':
    rf = ReadFile('HF_input.csv')
