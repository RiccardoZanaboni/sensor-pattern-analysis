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


def set_figure():
    figure = plt.figure()
    figure.set_dpi(100)
    figure.set_size_inches(configurator["info"]["figure_size"][0], configurator["info"]["figure_size"][1])
    return figure


def set_image_background():
    img = plt.imread(configurator["image"]["file"])
    ax.imshow(img, extent=[configurator["image"]["position"][0], configurator["image"]["position"][1],
                           configurator["image"]["position"][2], configurator["image"]["position"][3]])


def init_apartment(ax, config):
    ap = {}
    dic = config["apartment"]

    for room in dic:
        ap[room] = (dic[room][0], dic[room][1])

    return ax, ap


def set_time(i):
    time.set_text("Time : " + str(df["Time"][i]))


def animation_logic(i):
    person.center = apartment[df.iloc[i, 6]]
    set_time(i)
    set_probability(i)
    set_ev_level(i)
    filter_output.center = get_filter_output(i)


def init_filter():
    animation_logic(0)
    ax.add_patch(person)
    ax.add_patch(filter_output)
    return person, prob, filter_output, ev_level, time


def set_probability(index):
    text = ""
    separator = "\n"
    for room_bel in configurator["probability_position"]:
        text = text+separator + room_bel + ":" + '%.3f' % df[room_bel][index]
    prob.set_text(text)


def set_ev_level(index):
    float_value = float(df_filter.iloc[index, 1])
    value = '%.3f' % float_value
    text = "Evaluation level : " + value
    ev_level.set_text(text)
    dic = configurator["evaluation_thresholds"]
    for r in dic:
        if dic[r][1] >= float_value >= dic[r][0]:
            filter_output.set_color(r)
            return


def animate_filter(i):
    animation_logic(i)
    return person, prob, filter_output, ev_level, time


def get_filter_output(i):

    max_room = df.iloc[i, :][step:].apply(float).idxmax()
    room = configurator["room_dictionary"][max_room]
    return apartment[room]


def set_sensor_output(i):
    series = df.iloc[i][1:len(configurator["probability_position"])+1]
    text = "Sensors output"
    for column, val in series.iteritems():
        text = text + "\n" + column + " : " + str(val)
    sensor_output.set_text(text)


def init():
    person.center = apartment[df.iloc[0, 6]]
    set_sensor_output(0)
    set_time(0)
    ax.add_patch(person)
    return person, sensor_output, time


def animate(i):
    person.center = apartment[df.iloc[i, 6]]
    set_sensor_output(i)
    set_time(i)
    return person, sensor_output, time


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Chiamare il programma in maniera corretta")
        sys.exit(1)

    configurator = open_json(sys.argv[2])
    fig = set_figure()

    ax = plt.axes(xlim=(configurator["info"]["x_lim"][0], configurator["info"]["x_lim"][1]),
                  ylim=(configurator["info"]["y_lim"][0], configurator["info"]["x_lim"][1]))

    ax, apartment = init_apartment(ax, configurator)
    set_image_background()

    person = plt.Circle((2, 2), configurator["info"]["person_radius"], fc='b')
    time = plt.text(configurator["time"]["position"][0], configurator["time"]["position"][1], "",
                    fontsize=configurator["time"]["font_size"])

    if sys.argv[1] == "-f":
        df = read_file(configurator["info"]["input_file"])
        prob = plt.text(configurator["text_area"]["position"][0],
                        configurator["text_area"]["position"][1], "", fontsize=configurator["text_area"]["font_size"])
        ev_level = plt.text(configurator["ev_level"]["position"][0], configurator["ev_level"]["position"][1], "",
                            fontsize=configurator["ev_level"]["font_size"])

        filter_output = plt.Circle((0, 0), 1, fc='w', alpha=0.5)
        df_filter = read_file(configurator["info"]["evaluation_file"])
        step = len(configurator["probability_position"])+2
        gt_column_name = configurator["info"]["ground_truth_column_name"]
        anim = animation.FuncAnimation(fig, animate_filter, init_func=init_filter, frames=len(df.index)-1,
                                       interval=configurator["info"]["time_speed"], blit=True, repeat=False)

    if sys.argv[1] == "-s":
        df = read_file(configurator["info"]["input_file_s"])
        sensor_output = plt.text(configurator["text_area_s"]["position"][0],
                        configurator["text_area_s"]["position"][1], "Sensors output",
                                 fontsize=configurator["text_area_s"]["font_size"])

        anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(df.index) - 1,
                                       interval=configurator["info"]["time_speed"], blit=True, repeat=False)

    plt.show()

