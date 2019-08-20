import datetime
import pandas as pd
import Read_configurations

"""It unify the measures of all MovementState file"""


def read_file(file_name):
    df = pd.read_csv(file_name, ",")
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df = df[df['Timestamp'] >= datetime.datetime.strptime(
        Read_configurations.open_json()["input_unify_ms"]["starting_time"], "%Y-%m-%d %H:%M:%S")]
    return df


def write_file(df, file_name):
    df.sort_values(by=['Timestamp'], inplace=True, ascending=True)
    df.to_csv(file_name, index=False)


if __name__ == "__main__":
    file_names = Read_configurations.open_json()["input_unify_ms"]["file"]
    directory = Read_configurations.open_json()["input_unify_ms"]["directory"]

    df = read_file(directory+file_names[0])
    for file in file_names[1:5]:
        df = df.append(read_file(directory+file), ignore_index=True)

    write_file(df, Read_configurations.open_json()["output_unify_ms"]["directory"] +
                   Read_configurations.open_json()["output_unify_ms"]["file_out_name"])
