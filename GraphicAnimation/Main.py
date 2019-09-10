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
        ap[room] = (dic[room][0], dic[room][1])

    return ax, ap


def init_filter():
    person.center = apartment[df.iloc[0, 6]]
    set_probability(0)
    ax.add_patch(person)
    return person, prob


def set_probability(index):
    text = ""
    separator = "\n"
    for room_bel in configurator["probability_position"]:
        text = text+separator + room_bel + ":" + '%.3f' % df[room_bel][index]
    prob.set_text(text)


def init():
    person.center = apartment[df.iloc[0, 6]]
    ax.add_patch(person)
    return person,


def animate_filter(i):
    person.center = apartment[df.iloc[i, 6]]
    set_probability(i)
    return person, prob


def animate(i):
    person.center = apartment[df.iloc[i, 6]]
    return person,


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Chiamare il programma in maniera corretta")
        sys.exit(1)

    configurator = open_json(sys.argv[2])

    fig = plt.figure()
    fig.set_dpi(100)
    fig.set_size_inches(configurator["info"]["figure_size"][0], configurator["info"]["figure_size"][1])

    ax = plt.axes(xlim=(configurator["info"]["x_lim"][0], configurator["info"]["x_lim"][1]),
                  ylim=(configurator["info"]["y_lim"][0], configurator["info"]["x_lim"][1]))

    ax, apartment = init_apartment(ax, configurator)
    img = plt.imread(configurator["image"]["file"])
    ax.imshow(img, extent=[configurator["image"]["position"][0], configurator["image"]["position"][1],
                           configurator["image"]["position"][2], configurator["image"]["position"][3]])

    df = read_file(configurator["info"]["input_file"])

    person = plt.Circle((2, 2), configurator["info"]["person_radius"], fc='b')

    if sys.argv[1] == "-f":
        prob = plt.text(configurator["text_area"]["position"][0],
                        configurator["text_area"]["position"][1], "", fontsize=configurator["text_area"]["font_size"])

        anim = animation.FuncAnimation(fig, animate_filter, init_func=init_filter, frames=len(df.index)-1,
                                       interval=configurator["info"]["time_speed"], blit=True, repeat=False)

    plt.show()

