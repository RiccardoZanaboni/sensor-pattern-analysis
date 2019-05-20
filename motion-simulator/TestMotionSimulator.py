# Motion Simulator : simulate human's movement in an apartment from START_TIME to STOP_TIME
import Human as human
import pandas as pd
import Simulate_Time as st
import NormalDDP as model
import config

def sensor_sample(apartment, current_time, mat):
    """
    make the sensor sample

    :param apartment: list of Room
        the rooms in the apartment
    :param current_time: int
        the timer of the system
    :param mat: Human
        the person in the house
    :return:
    """
    for i in apartment:
        i.alert_sensor(current_time, mat)


def simulate(movement_tracker, current_time, mat):
    while current_time < STOP_TIME:

        if current_time == mat.time_next_move:
            mat.move(current_time)                          # if timer is equal to human's timer-decision : human moves
            movement_tracker = movement_tracker.append({'Time': current_time, 'Room': mat.current_room.name},
                                                       ignore_index=True)

        sensor_sample(apartment, current_time, mat)
        current_time = st.increase_time(current_time)

    return movement_tracker,current_time, mat


if __name__ == "__main__":

    configurator = config.SystemConfig()
    START_TIME = configurator.init_start_time()
    STOP_TIME = configurator.init_stop_time()
    current_time = START_TIME
    apartment = configurator.create_apartment()
    movement_tracker = pd.DataFrame(columns=['Time', 'Room'])
    normal_model = model.NormalDDP(configurator.init_mean(), configurator.init_std(), configurator.init_seed())
    mat = human.Human(apartment, normal_model)
    mat.chose_start_room()
    sensor_sample(apartment, current_time, mat)
    movement_tracker = movement_tracker.append({'Time': current_time, 'Room': mat.current_room.name}, ignore_index=True)
    current_time = st.increase_time(current_time)
    mat.time_next_move = current_time               # synchronisation of human's timer to the system clock

    ret = simulate(movement_tracker, current_time, mat)

    ret[0].to_csv("out.csv", index=False)
    ret[2].current_room.sensor.gateway.dataframe.to_csv("out_sensors.csv", index=False)

