import Simulate_Time as st
import pandas as pd
import datetime as dt
import hlt_state

file_name = "/home/mattia/Documents/Tesi/data2/hlt/hlt_29.csv"
SAMPLE_TIME = 10
MAX_EQUAL_SAMPLES = 10
index = 0


fsm_states = pd.DataFrame(columns=['Timestamp', 'HumidityState', 'LuminescenceState', 'TemperatureState'])

temperature_sensor = hlt_state.HltState(file_name)      # una macchina a stati per ciascun sensore
luminescence_sensor = hlt_state.HltState(file_name)
humidity_sensor = hlt_state.HltState(file_name)
MAX_TIMER = 3 * temperature_sensor.st_mean              # settaggio soglia in funzione della media campionamento
                                                        # dello specifico device.
                                                        # Ne uso uno perchè campionamento è sincrono per tutti i sensori
                                                        # dello stesso device


def read_samples():
    return pd.read_csv(file_name, ",")


def compare_samples(df, sensor, i):

    current_values = df.iloc[[index]].iat[0, i+1]
    if current_values == sensor.previous_sample:
        sensor.n_of_equals += 1
        return True
    else:
        sensor.previous_sample = current_values
        sensor.n_of_equals = 0
        return False


def update_fsm_states(sensors):
    global current_ts
    global fsm_states

    fsm_states = fsm_states.append({'Timestamp': current_ts,'HumidityState': sensors[0].state,
                                    'LuminescenceState': sensors[1].state,
                                    'TemperatureState': sensors[2].state}, ignore_index=True)


def check_dataframe(current_ts, df, sensor, i):

    global temp_states

#    state = READING
    timestamp_sample = dt.datetime.strptime(df.iat[index, 0], "%Y-%m-%d %H:%M:%S")  # taking the data of the sample
    if current_ts == timestamp_sample:      # equal to "missing_sample = false"
        sensor.timer = 0
        tmp = compare_samples(df, sensor, i)
        if tmp and sensor.n_of_equals < MAX_EQUAL_SAMPLES:                              # equal to "last_sample == sample"
            sensor.state = sensor.WARNING_EQUAL_MEASURES

        elif tmp and sensor.n_of_equals >= MAX_EQUAL_SAMPLES:   # equal to "last_sample == sample"
            sensor.state = sensor.NOT_WORKING

        else:                               # equal to "last sample != sample"
            sensor.state = sensor.WORKING
        return True
    else:                               # equal to "missing sample = true"
        if sensor.timer <= MAX_TIMER:
            sensor.state = sensor.WARNING_NOT_SAMPLE

        else:
            sensor.state = sensor.NOT_WORKING

        return False


if __name__ == '__main__':

    sensors = [humidity_sensor, luminescence_sensor, temperature_sensor]
    df = read_samples()                                                      # create a df to store the machine's states
    delta = dt.timedelta(minutes=SAMPLE_TIME)
    last_date = dt.datetime.strptime(df.tail(1).iat[0, 0], "%Y-%m-%d %H:%M:%S")     # extracting only the timestamp from
                                                                                    # the dataframe

    previous_time = df.head(1).iat[0, 0]                            # last sample read by the hlt sensor

    # initialysing the previous sample read 10 minutes before  the first sample in the csv file
    previous_time = dt.datetime.strptime(previous_time, "%Y-%m-%d %H:%M:%S") - delta
    current_ts = previous_time
    # initialyzing df of the machine's state
    fsm_states = fsm_states.append({'Timestamp': current_ts, 'HumidityState': humidity_sensor.state,
                                    'LuminescenceState': luminescence_sensor.state,
                                    'TemperatureState': temperature_sensor.state}, ignore_index=True)


#    last_date = dt.datetime.strptime("2018-12-14 18:00:00", "%Y-%m-%d %H:%M:%S")    # test mode only

    while current_ts <= last_date:
        current_ts = st.increase_time(current_ts)
        for i in range(0, len(sensors)):
            sensors[i].update_timer()                #  adding one minute
        if current_ts - previous_time == delta:      # checking every sample_time
            previous_time = current_ts
            tmp = [0, 0, 0]
            temp_states = []
            for i in range(0, len(sensors)):
                tmp[i] = check_dataframe(current_ts, df, sensors[i], i)
            update_fsm_states(sensors)
            if any(tmp):
                index += 1
    fsm_states.to_csv("/home/mattia/Documents/Tesi/data2/hlt/fsm_hlt_29.csv", index=False)
