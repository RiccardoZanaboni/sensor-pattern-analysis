import pandas as pd
import functools
import datetime
import Read_configurations

""" It create HLT file from the original data file from the gateway"""


def read_file(file_name, index):
    measures = pd.read_csv(file_name,",", usecols=['Date', 'Time', 'Class', 'Value'])

    measures = measures[measures['Class'] != "MovementState"]
    measures["Timestamp"] = measures["Date"].map(str)+" " + measures["Time"].map(str)
    measures = measures.drop(columns=["Date", "Time"])
    measures["Timestamp"] = measures['Timestamp'].apply(lambda x: datetime.datetime.strptime(x, "%d/%m/%Y %H:%M:%S"))
    list_of_dataframe = [df for df_name, df in measures.groupby('Class')]
    t = functools.reduce(lambda x, y: pd.merge(x, y, on=['Timestamp'], how="outer"),  list_of_dataframe)

    t.rename(columns={"Value_x": "HumidityMeasurementState", "Value_y": "LuminescenceState", "Value": "TemperatureState"}, inplace=True)
    t = t.drop(columns=["Class_x", "Class_y", "Class"])
    t = t[['Timestamp', 'HumidityMeasurementState', 'LuminescenceState', 'TemperatureState']]
    t = t.sort_values(by=['Timestamp'], ascending=True)

    t.to_csv(Read_configurations.open_json()["output_create_hlt"]["directory"] +
             Read_configurations.open_json()["output_create_hlt"]["file"][index], index=False)


if __name__ == "__main__":
    directory = Read_configurations.open_json()["input"]["directory"]
    files = Read_configurations.open_json()["input"]["file"]
    for i in range(0, len(files)):
        read_file(directory+files[i],i)
