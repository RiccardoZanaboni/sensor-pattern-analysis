import Human as human
import pandas as pd
import Time as t
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


def simulate(movement_tracker, time, mat, sensor_sample_time):
    """
    simulate the movement of the person

    :param movement_tracker: pandas.DataFrame
        dataframe of the person's movements
    :param time: float
        time of the system
    :param mat: Human
        the person in the apartment
    :param sensor_sample_time: float
        sensor sample time
    :return: tuple
        the DataFrame completed and the person
    """
    time_next_sample = time.START_TIME + sensor_sample_time

    while time.current_time < time.STOP_TIME:

        if time.check_time_delta(time.current_time, mat.time_next_move):
            mat.move(time.current_time)                          # if timer is equal to human's timer-decision : human moves
            movement_tracker = movement_tracker.append({'Time': time.current_time, 'Room': mat.current_room.name},
                                                       ignore_index=True)

        if time.check_time_delta(time.current_time, time_next_sample):
            sensor_sample(apartment, time.current_time, mat)
            time_next_sample = time.current_time + sensor_sample_time

        time.increase_time()

    return movement_tracker, mat


if __name__ == "__main__":

    configurator = config.SystemConfig()
    time = t.Time(configurator.init_start_time(), configurator.init_stop_time(), configurator.init_time_epsilon(),
                   configurator.init_system_time_delta())

    sensor_sample_time = configurator.init_sensor_sample_time()
    apartment = configurator.create_apartment()
    movement_tracker = pd.DataFrame(columns=['Time', 'Room'])
    normal_model = model.NormalDDP(configurator.init_mean(), configurator.init_std(), configurator.init_seed())
    mat = human.Human(apartment, normal_model)
    mat.chose_start_room()
    sensor_sample(apartment, time.current_time, mat)
    movement_tracker = movement_tracker.append({'Time': time.current_time, 'Room': mat.current_room.name},
                                               ignore_index=True)
    time.increase_time()

    ret = simulate(movement_tracker, time, mat, sensor_sample_time)

    ret[0].to_csv("out.csv", index=False)
    ret[1].current_room.sensor.gateway.dataframe.to_csv("out_sensors.csv", index=False)


