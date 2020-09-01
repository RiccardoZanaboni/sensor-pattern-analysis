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


def set_up(data_config, results_path):
    data = ReadFile.ReadFile(results_path / data_config["info"]["output_file_name"]).df
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


def df_histogram(config, efficiencies):
    """funzione per il calcolo dell'istogramma che verifica in quale intervallo
    cadono i valori di efficienza in base al quantum specificato in configurazione"""

    dfh = pd.DataFrame(columns=['Row_index', 'Interval', 'Efficiencies_count'])
    h_quantum = config['info']['histogram_quantum']
    number_of_intervals = int(1 / h_quantum)
    values_counter = []
    for i in range(number_of_intervals):  # inizializzo il valore dei contatori degli intervalli a 0
        values_counter.append(0)
    for i in range(len(efficiencies)):
        interval_min = 0
        interval_max = h_quantum
        for j in range(number_of_intervals):
            if ((efficiencies[i] <= interval_max) & (efficiencies[i] > interval_min)) | (j == number_of_intervals - 1):
                values_counter[j] += 1
                break
            interval_min += h_quantum
            interval_max += h_quantum

    interval_min = 0
    interval_max = h_quantum
    for k in range(number_of_intervals):
        cop_values = {'Row_index': k,
                      'Interval': str(format(interval_min, '.2f')) + '-' + str(format(interval_max, '.2f')),
                      'Efficiencies_count': values_counter[k]}
        dfh = dfh.append(cop_values, ignore_index=True)
        interval_min += h_quantum
        interval_max += h_quantum
    return dfh

def calc_percentage(dfh, efficiencies):
    """la funziona calcola la percentuale dei valori che cadono in ogni intervallo rispetto alla totalità
    dei valori di efficienza"""

    num_values = len(efficiencies)
    percentages = []

    for count in dfh['Efficiencies_count']:
        percentage = (count*100)/num_values
        percentages.append(percentage)

    return percentages


if __name__ == "__main__":
    # if len(sys.argv) < 2:
    #    print("Manca il nome del file json")
    #    sys.exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    config_path = Path(args.path)

    config = open_json(config_path)
    results_path = Path(config["info"]["results_path"])
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
    efficiencies = []
    n_correct = 0
    while i < len(data.index):
        max_room = found_max(data.iloc[i], config)
        state = data.loc[i, dictionary_rooms[data.loc[i, 'Room']]] / max_room
        temp = {'Time': data.loc[i, 'Time'], 'Efficiency': state}
        efficiencies.append(state)
        df = df.append(temp, ignore_index=True)
        i += 1

    dfh = df_histogram(config, efficiencies)
    percentages = calc_percentage(dfh, efficiencies)    #calcolo delle percentuali dei valori dell'istogramma sul totale

    df.to_csv(results_path / config["info"]["output_evaluation"], index=False)
    dfh.to_csv(results_path / config["info"]["output_histogram"], index=False)

    ax = plt.gca()
    df.plot(kind='line', x='Time', y='Efficiency', ax=ax)
    plt.savefig(results_path / config["info"]["img_evaluation"])

    # plot dell'istogramma
    width = 0.7  # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()

    ax.bar(dfh['Interval'], dfh['Efficiencies_count'], width, label='Intervals')

    ax.set_ylabel('Count of efficiency values')
    ax.set_xlabel('Intervals')
    ax.set_title('Scores divided by intervals')
    ax.legend()

    plt.xticks(rotation=-25)
    plt.savefig(results_path / config["info"]["img_histogram"])
