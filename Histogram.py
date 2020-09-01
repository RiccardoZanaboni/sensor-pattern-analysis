from pathlib import Path
import argparse
import pandas as pd
import json
import matplotlib.pyplot as plt

def do_total_count(path):
    global data, df
    for element in path.iterdir():
        if element.match('*.json'):
            with open(element, 'r') as filejson:
                data = json.load(filejson)

    intervals = int(1/data['info_HF']['histogram_quantum'])
    #inizializzo di 0 i count
    total_count = []
    for i in range(intervals):
        total_count.append(0)
    path = path / Path('results')
    for directory in path.iterdir():
        for file in directory.iterdir():
            if file.match('output_histogram*'):
                df = pd.read_csv(file)
                counts = df['Efficiencies_count']
                total_count += counts
    df['Efficiencies_count'] = total_count
    return df

#def calculate_percentage()


def init_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('configs_path', action='store', type=str,
                        help='Path of the base configuration relative to your current position')
    return parser

if __name__ == '__main__':
    parser = init_argparser()
    args = parser.parse_args()
    config_path = Path(args.configs_path)

    df = do_total_count(config_path)
    df.to_csv('Total_histogram.csv', index=False)

    width = 0.7  # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()

    ax.bar(df['Interval'], df['Efficiencies_count'], width, label='Intervals')

    ax.set_ylabel('Count of efficiency values')
    ax.set_title('Scores divided by interval')
    ax.legend()

    plt.xticks(rotation=-25)
    plt.savefig('Total_histogram.png')