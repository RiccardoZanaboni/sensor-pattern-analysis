# Motion Simulator : simulate human's movement in an apartment from START_TIME to STOP_TIME

import Room as room
import Human as human
import pandas as pd
import Simulate_Time as st
import MotionNormalDDP as model
import json
import Sensor
import Gateway


def create_apartment(data_config):
    apartment = []

    g = Gateway.Gateway(pd.DataFrame(columns=['Time', 'Room', 'State']))

    for i in data_config["room"]:
        tmp = room.Room(i, 0, Sensor.Sensor(i, data_config['other']['time_sample'], g))
        apartment.append(tmp)

    for i in apartment:
        i.adjacencies = []
        for room_name in data_config["room"][i.name]:
            for j in apartment:
                if room_name == j.name:
                    i.adjacencies.append(j)

    return apartment


if __name__ == "__main__":
    with open("configurations.json") as json_config:
        configurations = json.load(json_config)
    json_config.close()
    START_TIME = configurations["other"]["START_TIME"]
    STOP_TIME = configurations["other"]["STOP_TIME"]
    current_time = START_TIME
    apartment = create_apartment(configurations)                #lista delle stanze
    movement_tracker = pd.DataFrame(columns=['Time', 'Room'])
    normal_model = model.MotionNormalDDP(configurations["other"]["mu"], configurations["other"]["std"], configurations["other"]["seed"])
    mat = human.Human(apartment, normal_model)
    mat.chose_start_room()
    for i in apartment:
        i.alert_sensor(current_time, mat)
    movement_tracker = movement_tracker.append({'Time': current_time, 'Room': mat.current_room.name}, ignore_index=True)
    current_time = st.increase_time(current_time)
    mat.time_next_move = current_time               # synchronisation of human's timer to the system clock

    while current_time < STOP_TIME:

        if current_time == mat.time_next_move:
            mat.move(current_time)                          # if timer is equal to human's timer-decision : human moves
            movement_tracker = movement_tracker.append({'Time': current_time, 'Room': mat.current_room.name},
                                                       ignore_index=True)

        for i in apartment:
            i.alert_sensor(current_time, mat)

        current_time = st.increase_time(current_time)

    movement_tracker.to_csv("out.csv", index=False)
    mat.current_room.sensor.gateway.dataframe.to_csv("out_sensors.csv", index=False)

