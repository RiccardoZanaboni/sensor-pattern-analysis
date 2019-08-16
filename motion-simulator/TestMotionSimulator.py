import Human as human
import pandas as pd
import Time as t
import UniformDDP as ddp
import config
import SimulationInfo as si


def sensor_sample(apartment, current_time, mat, gateway):
    """
    make the sensor sample

    :param apartment: list of Room
        the rooms in the apartment
    :param current_time: int
        the timer of the system
    :param mat: Human
        the person in the house
    :param gateway: gateway
        system to store the data
    :return:
    """

    states = []
    for i in apartment:
        i.alert_sensor(current_time, mat)
        states.append(i.sensor.state)
    gateway.update_df_HF(current_time, states)


def simulate(movement_tracker, time, mat, sensor_sample_time, gateway):
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
            mat.move(time.current_time)                     # if timer is equal to human's timer-decision : human moves
            movement_tracker = movement_tracker.append({'Time': time.truncate(time.current_time, 3),
                                                        'Room': mat.current_room.name},
                                                       ignore_index=True)

        if time.check_time_delta(time.current_time, time_next_sample):
            sensor_sample(apartment, time.current_time, mat, gateway)
            time_next_sample = time.current_time + sensor_sample_time

        time.increase_time()

    return movement_tracker, mat


def check_running_mode(configurator):

    if configurator.init_test_mode() == "on":
        print("Running in test mode...")
    else:
        print("Simulating...")


def create_simulation_info(model):

    print("Creating simulation info file....")
    sim_info = si.SimulationInfo(model[0].seed, model[1].seed)
    sim_info.create_file()


if __name__ == "__main__":
    configurator = config.SystemConfig()
    check_running_mode(configurator)

    time = t.Time(configurator.init_start_time(), configurator.init_stop_time(), configurator.init_time_epsilon(),
                  configurator.init_system_time_delta())

    sensor_sample_time = configurator.init_sensor_sample_time()
    apartment, gateway = configurator.create_apartment()
    movement_tracker = pd.DataFrame(columns=['Time', 'Room'])
    model = [ddp.UniformDDp(configurator.init_long_model_lower(), configurator.init_long_model_upper(),
                            configurator.init_long_model_seed(), configurator.init_test_mode()),
             ddp.UniformDDp(configurator.init_short_model_lower(), configurator.init_short_model_upper(),
                            configurator.init_short_model_seed(), configurator.init_test_mode())]
    mat = human.Human(apartment, model)
    mat.chose_start_room(configurator.init_p_of_staying(), configurator.init_p_type_behaviour())
    sensor_sample(apartment, time.current_time, mat, gateway)
    movement_tracker = movement_tracker.append({'Time': time.current_time, 'Room': mat.current_room.name},
                                               ignore_index=True)
    time.increase_time()

    ret = simulate(movement_tracker, time, mat, sensor_sample_time, gateway)

    ret[0].to_csv("out.csv", index=False)
    ret[1].current_room.sensor.gateway.dataframe.to_csv("out_sensors.csv", index=False)
    gateway.df_HF.to_csv("HF_input.csv", index=False)

    create_simulation_info(model)

