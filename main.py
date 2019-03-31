import Simulate_Time as st
import pandas as pd
import datetime as dt
import numpy
import hlt_state


SAMPLE_TIME = 10
MAX_MISSED_SAMPLES = 3
MAX_EQUAL_SAMPLES = 5
index = 0

fsm_states = pd.DataFrame(columns=['Timestamp', 'State'])
hlt_sensor = hlt_state.HltState()


def read_samples():
    return pd.read_csv("hlt_4.csv", ",")


def compare_samples(df):

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


def update_fsm_states():
    global current_ts
    global fsm_states
    fsm_states = fsm_states.append({'Timestamp': current_ts, 'State': hlt_sensor.state}, ignore_index=True)


def check_dataframe(current_ts, df):

    global index

#    state = READING
    timestamp_sample = dt.datetime.strptime(df.iat[index, 0], "%Y-%m-%d %H:%M:%S")  # taking the data of the sample
    if current_ts == timestamp_sample:      # equal to "missing_sample = false"
        hlt_sensor.n_missing = 0
        tmp = compare_samples(df)
        if tmp and hlt_sensor.n_of_equals < MAX_EQUAL_SAMPLES:                              # equal to "last_sample == sample"
            hlt_sensor.state = hlt_sensor.WARNING_EQUAL_MEASURES
            update_fsm_states()
        elif tmp and hlt_sensor.n_of_equals >= MAX_EQUAL_SAMPLES:   # equal to "last_sample == sample"
            hlt_sensor.state = hlt_sensor.NOT_WORKING
            update_fsm_states()
        else:                               # equal to "last sample != sample"
            hlt_sensor.state = hlt_sensor.WORKING
            update_fsm_states()

        index += 1
    else:                               # equal to "missing sample = true"
        hlt_sensor.n_missing += 1
        if hlt_sensor.n_missing <= MAX_MISSED_SAMPLES:
            hlt_sensor.state = hlt_sensor.WARNING_NOT_SAMPLE
            update_fsm_states()
        else:
            hlt_sensor.state = hlt_sensor.NOT_WORKING
            update_fsm_states()


if __name__ == '__main__':
    # create a df to store the machine's states
    df = read_samples()
    delta = dt.timedelta(minutes=SAMPLE_TIME)
    # extracting only the timestamp from the dataframe
    last_date = dt.datetime.strptime(df.tail(1).iat[0, 0], "%Y-%m-%d %H:%M:%S")

    previous_time = df.head(1).iat[0, 0]  # last sample read by the hlt sensor

    # initialysing the previous sample read 10 minutes before  the first sample in the csv file
    previous_time = dt.datetime.strptime(previous_time, "%Y-%m-%d %H:%M:%S") - delta
    current_ts = previous_time
    # initialyzing df of the machine's state
    fsm_states = fsm_states.append({'Timestamp': current_ts, 'State': hlt_sensor.state}, ignore_index=True)


#    last_date = dt.datetime.strptime("2018-12-14 18:00:00", "%Y-%m-%d %H:%M:%S")    # test mode only

    while current_ts <= last_date:
        current_ts = st.increase_time(current_ts)  # adding one minute
        if current_ts - previous_time == delta:      # checking every sample_time
            previous_time = current_ts
            check_dataframe(current_ts, df)

    fsm_states.to_csv("fsm_hlt_4_beta.csv", index=False)
