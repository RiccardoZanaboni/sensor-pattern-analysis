import sys

import networkx as nx
from matplotlib import pyplot as plt
from matplotlib import animation
import utility
import numpy as np

""" There are two execution types :

 -Time triggered: to execute: python3 Main.py -time config.json 
 
 -Event triggered: to execute: python3 Main.py -evtr config.json """


def set_figure():
    figure = plt.figure()
    figure.set_dpi(100)
    figure.set_size_inches(configurator["info"]["figure_size"][0], configurator["info"]["figure_size"][1])
    return figure


def color_heat_map(i):
    dic = configurator["evaluation_thresholds"]
    rgba = configurator["rgba_tuple"]
    colormap = []
    for bel in df.iloc[i][len(configurator2["room"]) + 2:(len(configurator2["room"]) + 1) * 2]:
        for color in dic:
            if dic[color][1] >= bel >= dic[color][0]:  # se il valore  è compreso nella soglia setto il colore
                tupla=(rgba[color][0],rgba[color][1],rgba[color][2],rgba[color][3])
                colormap.append(tupla)
    nodes.set_color(colormap)


def set_probability(i):
    x = 0
    for bel in df.iloc[i][len(configurator2["room"]) + 2:(len(configurator2["room"]) + 1) * 2]:
        value = '%.3f' % bel
        probabilities[x].set_text(value)
        x += 1


def set_time(i):
    time.set_text("Time : " + str(df["Time"][i]))  # il tempo lo prendo da HF_out


def animation_logic(i):
    set_lamp_position(i)
    set_time(i)
    set_sensor_output(i)
    set_probability(i)
    color_heat_map(i)
    set_correct_room(i)
    set_ev_level(i)


def set_ev_level(index):
    float_value = float(df_filter.iloc[index, 1])  # prendo la colonna efficienza di output_evaluation
    value = '%.3f' % float_value
    text = "Evaluation level : " + value
    ev_level.set_text(text)


def set_correct_room(i):
    value = df["Room"][i]
    x = np.array(sizes)
    i=0
    for room in df.columns[1:len(configurator2["room"]) + 1]:
        if room==value:
            index=i
        i+=1
    x[index]=8500
    nodes.set_sizes(x)
    text = "Ground truth : " + value
    correct_room.set_text(text)


def set_sensors_lamp():
    image = plt.imread("lamp.png")
    return ax.imshow(image)

def set_lamp_position(i):
    x = 0
    series = df.iloc[i][1:len(configurator2["room"]) + 1]
    for room in df.columns[1:len(configurator2["room"]) + 1]:
        for column, val in series.iteritems():
            if (room == column):
                if (val == 1):
                    position = [pos[room][0] + 1.8, pos[room][1]]
                    img_extent = [position[0] + 1, position[0]+0.2, position[1] - 1, position[1]+0.2]
                    sensor_lamp[x].set_extent(img_extent)
                    sensor_lamp[x].set_visible(True)
                else:
                    sensor_lamp[x].set_visible(False)
        x += 1

def set_sensor_output(i):
    series = df.iloc[i][1:len(
        configurator2["room"]) + 1]  # iloc mi seleziona riga e colonna in questo caso prendo il valore dei sensori
    text = "Sensors output"
    for column, val in series.iteritems():  # iteritems va a iterare su un valore con pandas e mi da colonna e valore
        text = text + "\n" + column + " : " + str(val)
    sensor_output.set_text(text)  # metto il testo nelle posizioni che ho preso dal json prima nel main

def animate_filter(i):
    animation_logic(i)
    nodi = [nodes]
    ret_list = [sensor_output, ev_level, time, correct_room] + nodi + probabilities + sensor_lamp
    return ret_list

def animate_evtr(i):
    animation_logic(int(round(event["Time"][i])))

if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Chiamare il programma in maniera corretta")
        sys.exit(1)

    configurator = utility.open_json(sys.argv[2])
    fig = set_figure()  # setto dimensioni figura

    ax = plt.axes(xlim=(configurator["info"]["x_lim"][0], configurator["info"]["x_lim"][1]),
                  ylim=(
                      configurator["info"]["y_lim"][0], configurator["info"]["x_lim"][1]))  # definisco intervalle assi
    time = plt.text(configurator["time"]["position"][0], configurator["time"]["position"][1], "",
                    fontsize=configurator["time"]["font_size"])  # scelgo posizione e fontsize del tempo
    sensor_output = plt.text(configurator["text_area_s"]["position"][0],
                             configurator["text_area_s"]["position"][1], "Sensors output",
                             fontsize=configurator["text_area_s"]["font_size"])  # posizione output sensori
    configurator2 = utility.open_json(configurator["info"]["adj_file"])

    df = utility.read_file(configurator["info"]["input_file"])
    ev_level = plt.text(configurator["ev_level"]["position"][0], configurator["ev_level"]["position"][1], "",
                            fontsize=configurator["ev_level"]["font_size"])
    correct_room = plt.text(configurator["correct_room"]["position"][0],
                                configurator["correct_room"]["position"][1], "",
                                fontsize=configurator["correct_room"]["font_size"])
    G = nx.Graph()
    sensor_lamp = []
    sizes=[]
    for room in df.columns[1:len(configurator2["room"]) + 1]:
        sizes.append(3400)
        sensor_lamp.append(set_sensors_lamp())
        G.add_node(room)
    for room in df.columns[1:len(configurator2["room"]) + 1]:
        for adj in configurator2["room"][room]:
            G.add_edge(room, adj)
    pos = nx.spring_layout(G, center=[10, 13], scale=5)
    nodes = nx.draw_networkx_nodes(G, pos=pos, with_labels="true", node_size=3400, ax=ax)
    edges = nx.draw_networkx_edges(G, pos=pos, with_labels="true", ax=ax, font_size=80)
    labels = nx.draw_networkx_labels(G, pos=pos, font_size=17)
    probabilities = []
    for room in df.columns[1:len(configurator2["room"]) + 1]:
        probabilities.append(plt.text(pos[room][0] - 0.8, pos[room][1] - 0.9, "", fontsize=15))
    df_filter = utility.read_file(configurator["info"]["evaluation_file"])

    if sys.argv[1] == "-time":
        anim = animation.FuncAnimation(fig, animate_filter, frames=len(df.index) - 1,
                                       interval=configurator["info"]["time_speed"], blit=False,
                                       repeat=False)
        #  animate_filter è la funzione che viene richiamata ad ogni frame
    if sys.argv[1] == "-evtr":
        event=utility.read_file(configurator["info"]["event_file"])
        anim = animation.FuncAnimation(fig, animate_evtr, frames=len(event.index) - 1,
                                       interval=configurator["info"]["time_speed_evtr"], blit=False,
                                       repeat=False)
    plt.show()
