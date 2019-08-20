import pandas as pd
import datetime
import Read_configurations

""" It reads the original data file from the gateway and create a file with the MovementState measures only """


def read_sensor_file(file_name, index):
    df = pd.read_csv(file_name,",", usecols=['Date', 'Time', 'Class', 'Value'])

    df = df[df['Class'] == "MovementState"]
    df["Timestamp"] = df["Date"].map(str) + " " + df["Time"].map(str)
    df = df.drop(columns=["Date", "Time"])
    df["Timestamp"] = df['Timestamp'].apply(lambda x: datetime.datetime.strptime(x, "%d/%m/%Y %H:%M:%S"))
    df["Class"] = Read_configurations.open_json()["output_read_ms"]["class_name"][index]
    df.sort_values(by=['Timestamp'], inplace=True,ascending=True)

    df["Value"] = df["Value"].apply(lambda x : 1 if x == "isMoving" else 0)

    df.to_csv(Read_configurations.open_json()["output_read_ms"]["directory"] +
              Read_configurations.open_json()["output_read_ms"]["file"][index], index=False)


if __name__ == "__main__":
    directory = Read_configurations.open_json()["input"]["directory"]
    files = Read_configurations.open_json()["input"]["file"]
    for i in range(0, len(files)):
        read_sensor_file(directory+files[i], i)


