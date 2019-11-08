import datetime
import pandas as pd
import Read_configurations
import sys

"""It unify the measures of all MovementState file"""


def read_file(file_name, configurator):
    df = pd.read_csv(file_name, ",")
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df = df[df['Timestamp'] >= datetime.datetime.strptime(
        configurator["input_unify_ms"]["starting_time"], "%Y-%m-%d %H:%M:%S")]
    return df


def write_file(df, file_name):
    df.sort_values(by=['Timestamp'], inplace=True, ascending=True)
    df.to_csv(file_name, index=False)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Manca il nome del file json")
        sys.exit(1)

    configurator = Read_configurations.open_json(sys.argv[1])

    file_names = configurator["input_unify_ms"]["file"]
    directory = configurator["input_unify_ms"]["directory"]

    df = read_file(directory+file_names[0], configurator)
    for file in file_names[1:5]:
        df = df.append(read_file(directory+file,configurator), ignore_index=True)

    write_file(df, configurator["output_unify_ms"]["directory"] + configurator["output_unify_ms"]["file_out_name"])
