import json
import argparse
import numpy as np
from pathlib import Path
import sys

CONFIG_HF = "configurations_HF"
CONFIG_MS = "configurations_MS"
shell_script = "execute_configurations.sh"

def check_sum(prev_sum, sum):
    """controllo della somma dei valori di 0 e 1 che inserico nel vettore
    data['probability']['probability_of_short_moving_behaviour'] per far si che ci siano 0 e 1 di diverso numero"""

    if prev_sum != sum:
        return False
    return True

def insert_behaviour(data, person_num, prev_sum):
    """inserimento dei comportamenti in modo causale, ma in modo tale che da una simulazione a quella precedente
    i comportamenti siano diversi"""

    sum = 0
    condition = True
    while condition:
        data['probability']['probability_of_short_moving_behaviour'].clear()
        for i in range(person_num):
            # estrazione di 0 oppure di 1 che specificano il comportamewnto delle persone, 1= comportamento breve
            # 0 = comportamento lungo
            value = np.random.randint(0, 2)
            data['probability']['probability_of_short_moving_behaviour'].insert(i, value)
            sum += value
        condition = check_sum(prev_sum, sum)
    return sum

def create_configurations_HF(data_HF, output, n_config, path):
    """Crea la configurazione per l'histogram filter con le relative info"""

    if (path/Path(f'{CONFIG_HF}')).exists() == False:
        (path/Path(f'{CONFIG_HF}')).mkdir()

    data = {'info': data_HF['info_HF'], 'probability': data_HF['probability_HF'],
            'sensor_error_probability': data_HF['sensor_error_probability']}
    data['info']['results_path'] = f'{output}/config{n_config}_results'
    data['info']['input_file_name'] = f'HF_input_config{n_config}.csv'
    data['info']['ground_truth_file_name'] = f'out_config{n_config}.csv'
    data['info']['output_file_name'] = f'HF_out_config{n_config}.csv'
    data['info']['output_evaluation'] = f'output_evaluation_config{n_config}.csv'
    data['info']['img_evaluation'] = f'evaluate_config{n_config}.png'
    data['info']['img_histogram'] = f'histogram_config{n_config}.png'
    data['info']['output_histogram'] = f'output_histogram_config{n_config}.csv'

    with open(path/Path(f'{CONFIG_HF}/config{n_config}.json'), 'w') as filejson:
        json.dump(data, filejson)



def create_configuration_MS(init_output, data, path, n_config, person_number):
    """Crea la configurazione per il motion simulator con le relative info"""

    if (path/Path(f'{CONFIG_MS}')).exists() == False:
        (path/Path(f'{CONFIG_MS}')).mkdir()

    data['info']['person_number'] = person_number
    data['info']['output_simulator'] = f'HF_input_config{n_config}.csv'
    data['info']['output_movement'] = f'out_config{n_config}.csv'
    data['info']['output_sensors'] = f'out_sensors_config{n_config}.csv'
    data['info']['output_time'] = f'out_time_config{n_config}.csv'
    data['info']['output_path'] = f'{init_output}/config{n_config}_results'

    with open(path/Path(f'{CONFIG_MS}/config{n_config}.json'), 'w') as filejson:
        json.dump(data, filejson)


def generate(path, main_path):
    global data
    print('Generating Configurations...')
    n_config = 0
    for base_config in path.glob('*.json'):
        person_number = 0

        with open(base_config, 'r') as filejson:
            data = json.load(filejson)
            
        data_HF = data.copy()

        init_output = data['info']['output_path']
        [data.pop(key) for key in ['info_HF', 'probability_HF', 'sensor_error_probability']]
        [data_HF.pop(key) for key in ['room', 'time', 'probability', 'info']]

        if (path/Path(init_output)).exists() == False:
            (path / Path(init_output)).mkdir()

        for i in range(data['generator_info']['max_person_number']):  #
            prev_sum = -1
            person_number += 1
            for j in range(data['generator_info']['number_of_configurations']):
                n_config += 1
                prev_sum = insert_behaviour(data, person_number, prev_sum)
                create_configuration_MS(init_output, data, path, n_config, person_number)
                create_configurations_HF(data_HF, init_output, n_config, path)
                data['probability']['probability_of_short_moving_behaviour'].clear()

    print('Number of configurations generated: ', n_config)

    create_bash_script(path, data, n_config, main_path)


def create_bash_script(path, data, num_config, main_path):
    path_MS = path / Path('configurations_MS')
    conf_path = path.resolve()
    num_simulations = data['generator_info']['number_of_simulations']
    tot_sim = num_config*num_simulations          #numero totale di simulazioni all'interno del file execute_configurations.sh
    with open(conf_path/Path(shell_script), 'w') as f:
        HEADER = f"""#!/bin/bash 
MAINPATH={main_path}
CONFPATH={conf_path}
MAIN_EXE_MS={data["paths"]["main_MS"]}
MAIN_EXE_HF={data['paths']['main_HF']}
MAIN_EXE_EV={data['paths']['main_EV']}
MAIN_EXE_HIST={data['paths']['main_HIST']}

"""
        f.write(HEADER)

        i = 1
        for config in path_MS.glob('config*.json'):
            for n in range(num_simulations):
                BODY = f'''
echo "Simulation n.{i} out of {tot_sim}"
python3 $MAINPATH/$MAIN_EXE_MS {CONFIG_MS}/{config.stem}.json
python3 $MAINPATH/$MAIN_EXE_HF {CONFIG_HF}/{config.stem}.json
python3 $MAINPATH/$MAIN_EXE_EV {CONFIG_HF}/{config.stem}.json
echo "[$(date +\"%Y-%m-%d %T.%3N\")]" {config.stem} DONE | tee -a log_configurations.txt


'''
                f.write(BODY)
                i += 1
        histogram_command = f'''        
echo "Creating simulation total Histogram..."
python3 $MAINPATH/$MAIN_EXE_HIST $CONFPATH
'''
        f.write(histogram_command)

def init_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('configs_path', action='store', type=str,
                        help='Path of the base configuration relative to your current position')
    parser.add_argument('--projectdir', '-p', metavar='PROJECTDIR',
                        help='path relative to the project directory sensor-pattern-analysis')
    return parser



if __name__ == '__main__':
    parser = init_argparser()
    args = parser.parse_args()
    base_configs_path = Path(args.configs_path)

    if args.projectdir:
        # il percorso della directory del progetto viene messa in main_path se l'argomento opzionale viene inserito
        # allora uso quel percorso altrimenti utilizzo la directory corrente
        main_path = Path(args.projectdir)
    else:
        main_path = Path.cwd()
    correct_directory = False
    for file in main_path.iterdir():
        if file.name == "GenerateConfigurations.py":
            correct_directory = True
            break
    if not correct_directory:
        print("You are not in the correct directory! change project directory's path")
        sys.exit(1)

    generate(base_configs_path, main_path)