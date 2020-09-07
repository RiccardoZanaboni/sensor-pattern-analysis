import time


class SimulationInfo:
    """
    It tracks the information about the simulation
        ...
        Attributes
        lwt_seed : int
            the seed of the distribution from which the long time permanence in a room is extracted

        swt_seed : int
            the seed of the distribution from which the short time permanence in a room is extracted

        _file_name : str
            name of the file in which the simulation info are saved

        _directory : str
            name of the directory in which the simulation info files are saved

    """

    def __init__(self, lwt_seed, swt_seed, number_of_person):

        """
        :param int lwt_seed: the seed of the distribution from which the long time permanence in a room is extracted
        :param int swt_seed: the seed of the distribution from which the short time permanence in a room is extracted
        :param int number_of_person: number of person in the simulation

        """

        self.lwt_seed = lwt_seed
        self.swt_seed = swt_seed
        self._file_name = str(int(time.time()))
        self._directory_name = "simulation-info"
        self.number_of_person = number_of_person

    @property
    def lwt_seed(self):
        return self.__lwt_seed

    @lwt_seed.setter
    def lwt_seed(self, lwt_seed):
        self.__lwt_seed = lwt_seed

    @property
    def swt_seed(self):
        return self.__swt_seed

    @swt_seed.setter
    def swt_seed(self, swt_seed):
        self.__swt_seed = swt_seed

    @property
    def number_of_person(self):
        return self.__number_of_person

    @number_of_person.setter
    def number_of_person(self, number_of_person):
        self.__number_of_person = number_of_person

    def create_file(self):
        """
        It creates the file where the info of the simulation are saved
        :return:
        """
        file_name = self._directory_name+"/"+self._file_name+".txt"
        with open(file_name, "w+") as f:
            BODY = f"""Simulation Info :
Long waiting time seed : {self.lwt_seed}
Short  waiting time seed : {self.swt_seed}
"Number of person : {self.number_of_person}
"""
            f.write(BODY)

