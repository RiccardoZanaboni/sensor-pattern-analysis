import pandas as pd
import datetime
import Read_configurations
import sys

""" It reads the original data file from the gateway and create a file with the MovementState measures only """


def read_sensor_file(file_name, index, configurator):
    df = pd.read_csv(file_name,",", usecols=['Date', 'Time', 'Class', 'Value'])

    df = df[df['Class'] == "MovementState"]
    df["Timestamp"] = df["Date"].map(str) + " " + df["Time"].map(str)
    df = df.drop(columns=["Date", "Time"])
    df["Timestamp"] = df['Timestamp'].apply(lambda x: datetime.datetime.strptime(x, "%d/%m/%Y %H:%M:%S"))
    df["Class"] = configurator["output_read_ms"]["class_name"][index]
    df.sort_values(by=['Timestamp'], inplace=True,ascending=True)

    df["Value"] = df["Value"].apply(lambda x: 1 if x == "isMoving" else 0)

    df.to_csv(configurator["output_read_ms"]["directory"] +
              configurator["output_read_ms"]["file"][index], index=False)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Manca il nome del file json")
        sys.exit(1)

    configurator = Read_configurations.open_json(sys.argv[1])

    directory = configurator["input"]["directory"]
    files = configurator["input"]["file"]
    for i in range(0, len(files)):
        read_sensor_file(directory+files[i], i, configurator)


