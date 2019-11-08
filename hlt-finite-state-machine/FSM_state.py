import Simulate_Time as st
import pandas as pd
import datetime as dt
import numpy
import hlt_state
import Read_configurations
import sys


def read_samples(configurator):
    return pd.read_csv(configurator["info"]["path_directory_input_FSM"] + configurator["info"]["file_input_FSM"], ",")


def compare_samples(df, index):

    """compare the sensor last three measures with the current ones ; if they are equals,
       update the finite state machine counter for equals measures ,else it updates the sensor previous measure
       for future controls """

    current_values = []
    for i in range(3):
        current_values.append(df.iloc[[index]].iat[0, i+1])
    if numpy.array_equal(current_values, hlt_sensor.previous_sample):
        hlt_sensor.n_of_equals += 1
        return True
    else:
        hlt_sensor.previous_sample = current_values
        hlt_sensor.n_of_equals = 0
        return False


def update_fsm_states(current_ts):
    """update the DataFrame with timestamp of the measures and the finite state machine current state"""
    global fsm_states
    fsm_states = fsm_states.append({'Timestamp': current_ts, 'State': hlt_sensor.state}, ignore_index=True)


def check_dataframe(current_ts, df, index):
    """check if the input DataFrame contains a measure at the expected timestamp,if this condition is true check
        if the current sample is equals to the previous one, if not it updates
       the finite state machine counter for missing samples . Finally , it updates the output DataFrame"""

    timestamp_sample = dt.datetime.strptime(df.iat[index, 0], "%Y-%m-%d %H:%M:%S")  # taking the data of the sample
    if current_ts == timestamp_sample:      # equal to "missing_sample = false"
        hlt_sensor.timer = 0
        tmp = compare_samples(df, index)
        if tmp and hlt_sensor.n_of_equals < MAX_EQUAL_SAMPLES:                              # equal to "last_sample == sample"
            hlt_sensor.state = hlt_sensor.possible_states["WARNING_EQUAL_MEASURES"]
            update_fsm_states(current_ts)
        elif tmp and hlt_sensor.n_of_equals >= MAX_EQUAL_SAMPLES:   # equal to "last_sample == sample"
            hlt_sensor.state = hlt_sensor.possible_states["NOT_WORKING"]
            update_fsm_states(current_ts)
        else:                               # equal to "last sample != sample"
            hlt_sensor.state = hlt_sensor.possible_states["WORKING"]
            update_fsm_states(current_ts)

        index += 1
    else:                               # equal to "missing sample = true"
        if hlt_sensor.timer <= MAX_TIMER:
            hlt_sensor.state = hlt_sensor.possible_states["WARNING_NOT_SAMPLE"]
            update_fsm_states(current_ts)
        else:
            hlt_sensor.state = hlt_sensor.possible_states["NOT_WORKING"]
            update_fsm_states(current_ts)
    return index


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Manca il nome del file json")
        sys.exit(1)

    configurator = Read_configurations.open_json(sys.argv[1])

    hlt_sensor = hlt_state.HltState(configurator)
    MAX_TIMER = configurator["FSM_info"]["number_missing_sample"] * hlt_sensor.st_mean
    MAX_EQUAL_SAMPLES = configurator["FSM_info"]["MAX_EQUALS_SAMPLES"]
    fsm_states = pd.DataFrame(columns=['Timestamp', 'State'])
    index = 0

    df = read_samples(configurator)
    delta = dt.timedelta(minutes=configurator["FSM_info"]["SAMPLE_TIME"])

    last_date = dt.datetime.strptime(df.tail(1).iat[0, 0], "%Y-%m-%d %H:%M:%S")
    previous_time = df.head(1).iat[0, 0]  # last sample read by the hlt sensor
    previous_time = dt.datetime.strptime(previous_time, "%Y-%m-%d %H:%M:%S") - delta
    current_ts = previous_time

    fsm_states = fsm_states.append({'Timestamp': current_ts, 'State': hlt_sensor.state}, ignore_index=True)

    while current_ts <= last_date:
        current_ts = st.increase_time(current_ts)
        hlt_sensor.update_timer()
        if current_ts - previous_time == delta:
            previous_time = current_ts
            index = check_dataframe(current_ts, df, index)

    fsm_states.to_csv(configurator["info"]["path_directory_output_FSM"] +
                      configurator["info"]["file_output_FSM"], index=False)
