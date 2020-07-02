import sys

import ReadFile
import json
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import argparse

"""
    Script used to evaluate the output of the histogram filter after a simulation.
    It calculates the relative frequency between the number of time that the person is 
    in a room and the room is the one  the highest probability to be in for the histogram filter. 
"""


def open_json(file_name):
    with open(file_name) as json_config:
        data_config = json.load(json_config)
    json_config.close()
    return data_config


def set_up(data_config,results_path):
    data = ReadFile.ReadFile(results_path/data_config["info"]["output_file_name"]).df
    return data


"""
    Dictionary [key='the name of the room' : value='the index of the column with the probability of the room' 
"""


def dictionary_room(data_config):
    key = data_config["info"]["room_name"]
    value = data_config["info"]["columns_name"][1:]
    dictionary = {}
    for i in range(0, len(key)):
        dictionary[key[i]] = value[i]
    return dictionary


"""
    Found the max value between the probability of the rooms 
"""


def found_max(probability_arrrey: pd.Series, data_config):
    constant = len(data_config["info"]["state_domain"]) + 2
    val_max = probability_arrrey.iloc[constant:].apply(float).max()
    return val_max


if __name__ == "__main__" :
    #if len(sys.argv) < 2:
    #    print("Manca il nome del file json")
    #    sys.exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    config_path = Path(args.path)

    config = open_json(config_path)
    results_path = config_path.parents[2]/config["info"]["results_rel_path"]
    df = pd.DataFrame(columns=['Time', 'Efficiency'])

    n_same_config = 0
    first_stem = results_path.stem
    while (results_path / config["info"]["output_evaluation"]).exists() == True:
        n_same_config += 1
        stem = first_stem + '[' + str(n_same_config) + ']'
        results_path = results_path.parent
        results_path = results_path / stem

    data = set_up(config, results_path)
    i = 0
    dictionary_rooms = dictionary_room(config)
    n_correct = 0
    while i < len(data.index):
        max_room = found_max(data.iloc[i], config)
        state = data.loc[i, dictionary_rooms[data.loc[i, 'Room']]]/max_room
        temp = {'Time': data.loc[i, 'Time'],'Efficiency': state}
        df = df.append(temp, ignore_index=True)
        i += 1

    df.to_csv(results_path/config["info"]["output_evaluation"], index=False)

    ax = plt.gca()
    df.plot(kind='line', x='Time', y='Efficiency', ax=ax)
    plt.savefig(results_path/config["info"]["img_evaluation"])


