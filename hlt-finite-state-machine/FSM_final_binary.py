import pandas as pd
import Read_configurations
import sys


def binary_conversion(df):
    """convert output of final state machine in binary format(1--> working and warning 0-->not working)"""
    for i in range(0, df.shape[0]):
        if df.iat[i, 1] != 0:
            df.iat[i, 1] = 1
    return df


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Manca il nome del file json")
        sys.exit(1)

    configurator = Read_configurations.open_json(sys.argv[1])
    df = pd.read_csv(configurator["info"]["path_directory_input_final_binary"] +
                     configurator["info"]["file_input_final_binary"], ",")
    df = binary_conversion(df)
    df.to_csv(configurator["info"]["path_directory_output_final_binary"] +
              configurator["info"]["file_output_final_binary"], index=False)
