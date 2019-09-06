import ReadFile
import json
import pandas as pd
import matplotlib.pyplot as plt

"""
    Script used to evaluate the output of the histogram filter after a simulation.
    It calculates the relative frequency between the number of time that the person is 
    in a room and the room is the one  the highest probability to be in for the histogram filter. 
"""


def open_json():
    with open("config_ap_one.json") as json_config:
        data_config = json.load(json_config)
    json_config.close()
    return data_config


def set_up():
    data_config = open_json()
    data = ReadFile.ReadFile(data_config["info"]["output_file_name"]).df
    return data


"""
    Dictionary [key='the name of the room' : value='the index of the column with the probability of the room' 
"""


def dictionary_room():
    data_config = open_json()
    key = data_config["info"]["room_name"]
    value = data_config["info"]["columns_name"][1:]
    dictionary = {}
    for i in range(0, len(key)):
        dictionary[key[i]] = value[i]
    return dictionary


"""
    Found the max value between the probability of the rooms 
"""


def found_max(probability_arrrey: pd.Series):
    constant = len(open_json()["info"]["state_domain"]) + 2
    val_max = probability_arrrey.iloc[constant:].apply(float).max()
    return val_max


if __name__ == "__main__" :
    df = pd.DataFrame(columns=['Time', 'Efficiency'])
    data = set_up()
    i = 0
    dictionary_rooms = dictionary_room()
    n_correct = 0
    while i < len(data.index):
        max_room = found_max(data.iloc[i])
        state = data.loc[i, dictionary_rooms[data.loc[i, 'Room']]]/max_room
        temp = {'Time': data.loc[i, 'Time'],'Efficiency': state}
        df = df.append(temp, ignore_index=True)
        i += 1

    df.to_csv(open_json()["info"]["output_evaluation"], index=False)

    ax = plt.gca()
    df.plot(kind='line', x='Time', y='Efficiency', ax=ax)
    plt.savefig(open_json()["info"]["img_evaluation"])


