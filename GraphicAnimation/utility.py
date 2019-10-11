import pandas as pd
import json

def read_file(file_name):
    df = pd.read_csv(file_name, ',')
    return df


def open_json(file_name):
    with open(file_name) as json_config:
        data_config = json.load(json_config)
    json_config.close()
    return data_config
