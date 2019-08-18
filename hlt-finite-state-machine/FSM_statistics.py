import pandas as pd
import Read_configurations


def delta_timestamp(df, f, file_name):
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])              # Timestamp to Datetime

    df["Delta"] = df["Timestamp"].diff()                           # Caluclate delta between two consecutive timestamps
    df = df.dropna()
    df["Delta"] = df["Delta"].apply(lambda x: x.total_seconds())

    df_statistics = df.describe(percentiles=[0.25, 0.50, 0.75, 0.85, 0.90, 0.98])

    outliers_line = 3*df_statistics.loc['mean']['Delta']
    df = df[df['Delta'] < outliers_line]

    df_statistics = df.describe(percentiles=[0.25, 0.50, 0.75, 0.85, 0.90, 0.98])
    df_statistics = df_statistics['Delta']

    f.write(file_name+"\n")
    df_statistics.to_csv(f)


if __name__ == '__main__':
    file_name = Read_configurations.open_json()["info"]["input_FSM_statistics"]
    for t in range(0, len(file_name)):
        file_name[t] = Read_configurations.open_json()["info"]["directory_input_FSM_statistics"]+file_name[t]

    data_frame = []
    for k in range(0, len(file_name)):
        data_frame.append(pd.read_csv(file_name[k]))

    f = open(Read_configurations.open_json()["info"]["directory_output_FSM_statistics"]+
             Read_configurations.open_json()["info"]["output_FSM_statistics"], "w")
    f.close()
    f = open(Read_configurations.open_json()["info"]["directory_output_FSM_statistics"]+
             Read_configurations.open_json()["info"]["output_FSM_statistics"], "a")

    i = 0
    for j in range(0, len(data_frame)):
        delta_timestamp(data_frame[j], f, file_name[j])

    f.close()
