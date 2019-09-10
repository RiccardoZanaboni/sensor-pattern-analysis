import numpy as np
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


def init_apartment(ax):
    apartment = {"toilet": plt.Circle((2, 2), 1, fc='y'), "kitchen": plt.Circle((2, 8), 1, fc='y'),
                 "bedroom": plt.Circle((8, 2), 1, fc='y'), "livingroom": plt.Circle((8, 8), 1, fc='y'),
                 "atrium": plt.Circle((5, 5), 1, fc='y')}
    for i in apartment:
        ax.add_patch(apartment[i])
    return ax, apartment


def init():
    person.center = apartment[df.iloc[0, 1]].get_center()
    ax.add_patch(person)
    return person,


def animate(i):
    person.center = apartment[df.iloc[i, 1]].get_center()
    return person,


if __name__ == "__main__":

    fig = plt.figure()
    fig.set_dpi(100)
    fig.set_size_inches(7, 6.5)
    ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
    ax, apartment = init_apartment(ax)

    df = read_file("/home/mattia/Tesi/output_old_apartment/out.csv")

    person = plt.Circle((2, 2), 0.25, fc='b')

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(df.index)-1,
                                   interval=1000, blit=True, repeat=False)

    plt.show()

