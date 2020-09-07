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

def calc_percentage(df):

    total = 0
    counts_effic = df['Efficiencies_count']
    for count in counts_effic:
        total += count
    percentages = []
    for value in counts_effic:
        percentage = (value*100)/total
        percentages.append(percentage)

    return percentages

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
    percentages = calc_percentage(df)

    df.to_csv('Total_histogram.csv', index=False)

    width = 0.7  # the width of the bars: can also be len(x) sequence

    fig, ax = plt.subplots()

    ax.bar(df['Interval'], df['Efficiencies_count'], width, label='Intervals')

    ax.set_ylabel('Count of efficiency values')
    ax.set_title('Scores divided by interval')


    rects = ax.patches
    i = 0

    for rect in rects:
        y_value = rect.get_height()
        x_value = rect.get_x() + rect.get_width() / 2

        va = 'top'
        space = 10

        label = f'{format(percentages[i], ".2f")}%'

        plt.annotate(
            label,  # Use `label` as label
            (x_value, y_value),  # Place label at end of the bar
            xytext=(0, space),  # Vertically shift label by `space`
            textcoords="offset points",  # Interpret `xytext` as offset in points
            ha='center',  # Horizontally center label
            va=va)
        i += 1

    plt.xticks(rotation=-25)
    plt.savefig('Total_histogram.png')