import sys
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import animation
import json


def read_file(file_name):
    df = pd.read_csv(file_name, ',')
    return df


def open_json(file_name):
    with open(file_name) as json_config:
        data_config = json.load(json_config)
    json_config.close()
    return data_config


def init_apartment(ax, config):
    ap = {}
    dic = config["apartment"]

    for room in dic:
        ap[room] = plt.Circle((dic[room][0], dic[room][1]), dic[room][2], fc=config["info"]["default_room_color"])

    for i in ap:
        ax.add_patch(ap[i])

    return ax, ap


def init():
    person.center = apartment[df.iloc[0, 6]].get_center()
    ax.add_patch(person)
    return person,


def animate(i):
    person.center = apartment[df.iloc[i, 6]].get_center()
    return person,


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Manca il nome del file json")
        sys.exit(1)

    configurator = open_json(sys.argv[1])

    fig = plt.figure()
    fig.set_dpi(100)
    fig.set_size_inches(configurator["info"]["figure_size"][0], configurator["info"]["figure_size"][1])

    ax = plt.axes(xlim=(configurator["info"]["x_lim"][0], configurator["info"]["x_lim"][1]),
                  ylim=(configurator["info"]["y_lim"][0], configurator["info"]["x_lim"][1]))

    ax, apartment = init_apartment(ax, configurator)

    df = read_file(configurator["info"]["input_file"])

    person = plt.Circle((2, 2), configurator["info"]["person_radius"], fc='b')

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(df.index)-1,
                                   interval=configurator["info"]["time_speed"], blit=True, repeat=False)

    plt.show()

