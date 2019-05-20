import Room
import NormalDDP
import Gateway
import Sensor
import pandas as pd
import json


class SystemConfig:

    def __init__(self):
        with open("configurations.json") as json_config:
            self.data_config = json.load(json_config)
        json_config.close()

    @property
    def data_config(self):
        return self.__data_config

    @data_config.setter
    def data_config(self, data_config):
        self.__data_config = data_config

    def create_apartment(self):

        apartment = []

        g = Gateway.Gateway(pd.DataFrame(columns=['Time', 'Room', 'State']))

        for i in self.data_config["room"]:
            tmp = Room.Room(i, 0, Sensor.Sensor(i, g, NormalDDP.NormalDDP(self.data_config['other']['mu_sample_time'],
                                                                          self.data_config['other']['std_sample_time'],
                                                                          self.data_config['other']['seed_sample_time'])
                                                ))
            apartment.append(tmp)

        for i in apartment:
            i.adjacencies = []
            for room_name in self.data_config["room"][i.name]:
                for j in apartment:
                    if room_name == j.name:
                        i.adjacencies.append(j)

        return apartment

    def init_start_time(self):
        return self.data_config["other"]["START_TIME"]

    def init_stop_time(self):
        return self.data_config["other"]["STOP_TIME"]

    def init_mean(self):
        return self.data_config["other"]["mu_waiting_time"]

    def init_std(self):
        return self.data_config["other"]["std_waiting_time"]

    def init_seed(self):
        return self.data_config["other"]["seed_waiting_time"]
