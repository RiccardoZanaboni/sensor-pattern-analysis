import time


class SimulationInfo:
    """

    """

    def __init__(self, lwt_seed, swt_seed):
        self.lwt_seed = lwt_seed
        self.swt_seed = swt_seed
        self._file_name = str(int(time.time()))
        self._directory_name = "simulation-info"

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

    def create_file(self):
        file_name = self._directory_name+"/"+self._file_name+".txt"
        f = open(file_name, "w+")
        f.write("Simulation Info :"+"\n")
        f.write("Long  waiting time  seed : %d \n" % self.lwt_seed)
        f.write("Short  waiting time seed : %d \n" % self.swt_seed)
        f.close()

