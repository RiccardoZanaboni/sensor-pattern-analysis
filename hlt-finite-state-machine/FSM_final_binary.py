import pandas as pd
import Read_configurations


def binary_conversion(df):
    """convert output of final state machine in binary format(1--> working and warning 0-->not working)"""
    for i in range(0, df.shape[0]):
        if df.iat[i, 1] != 0:
            df.iat[i, 1] = 1
    return df


if __name__ == '__main__':
    df = pd.read_csv(Read_configurations.open_json()["info"]["path_directory_input_final_binary"]+
                                                    ["info"]["file_input_final_binary"], ",")
    df = binary_conversion(df)
    df.to_csv(Read_configurations.open_json()["info"]["path_directory_output_final_binary"]+
                                                    ["info"]["file_output_final_binary"],index=False)
