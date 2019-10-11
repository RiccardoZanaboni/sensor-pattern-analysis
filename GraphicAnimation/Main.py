import sys
from matplotlib import pyplot as plt
from matplotlib import animation
import utility


def set_figure():
    figure = plt.figure()
    figure.set_dpi(100)
    figure.set_size_inches(configurator["info"]["figure_size"][0], configurator["info"]["figure_size"][1])
    return figure


def set_background():
    circle = []
    for room in configurator["apartment"]:
        circle.append(plt.Circle(configurator["apartment"][room], 2, fc='y', alpha=0.25))

    for c in circle:
        ax.add_patch(c)

    return circle


def set_line():
    line = []
    for room in configurator["adj"]:
        line.append(plt.Line2D(room[0], room[1]))

    for l in line:
        ax.add_line(l)


def color_heat_map(i):
    room_list = configurator["probability_position"]

    def set_color(value, j):
        dic = configurator["evaluation_thresholds"]

        for r in dic:
            if dic[r][1] >= value >= dic[r][0]:
                ap_heat_map[j].set_color(r)
                return

    for index, room in enumerate(room_list):
        set_color(df[room][i], index)


def init_apartment(ax, config):
    ap = {}
    dic = config["apartment"]

    for room in dic:
        ap[room] = (dic[room][0], dic[room][1])

    return ax, ap


def set_person_image():
    image = plt.imread("person.png")
    return ax.imshow(image, extent=[0, 0, 0, 0])


def set_person_position(i):
    centre = apartment[df.iloc[i, 6]]
    img_extent = [centre[0] - 1, centre[0] + 1, centre[1] - 1, centre[1] + 1]
    person.set_extent(img_extent)
    # person.set_center(centre)


def set_apartment_heat_map():
    circles = []
    dic = configurator["apartment"]
    for i in dic:
        circles.append(plt.Circle(dic[i], 2, fc='white', alpha=0.25))
    for c in circles:
        ax.add_patch(c)
    return circles


def set_prob_value():
    text_area = []
    dic = configurator["prob_text_area"]

    for i in dic:
        text_area.append(plt.text(dic[i][0], dic[i][1], "", fontsize='14'))

    return text_area


def set_name():
    text_area = []
    dic = configurator["prob_text_name"]

    for i in dic:
        text_area.append(plt.text(dic[i][0], dic[i][1], i, fontsize='14'))

    return text_area


def set_time(i):
    time.set_text("Time : " + str(df["Time"][i]))


def animation_logic(i):
    set_person_position(i)
    set_time(i)
    set_sensor_output(i)
    set_probability(i)
    color_heat_map(i)
    set_ev_level(i)


def init_filter():
    line = []
    for room in configurator["adj"]:
        line.append(plt.Line2D(room[0], room[1]))

    for l in line:
        ax.add_line(l)

    for c in ap_heat_map:
        ax.add_patch(c)

    ret_list = [person, sensor_output, ev_level, time]+ap_heat_map+prob_value
    return ret_list


def set_probability(index):

    for j, room_bel in enumerate(configurator["probability_position"]):
        prob_value[j].set_text('%.3f' % df[room_bel][index])


def set_ev_level(index):
    float_value = float(df_filter.iloc[index, 1])
    value = '%.3f' % float_value
    text = "Evaluation level : " + value
    ev_level.set_text(text)


def animate_filter(i):
    animation_logic(i)
    ret_list = [person, sensor_output, ev_level, time] + ap_heat_map+prob_value
    return ret_list


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
    ret_list = [person, sensor_output, time] + graph
    return ret_list


def animate(i):
    set_person_position(i)
    set_sensor_output(i)
    set_time(i)
    ret_list = [person, sensor_output, time] + graph 
    return ret_list


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Chiamare il programma in maniera corretta")
        sys.exit(1)

    configurator = utility.open_json(sys.argv[2])
    fig = set_figure()

    ax = plt.axes(xlim=(configurator["info"]["x_lim"][0], configurator["info"]["x_lim"][1]),
                  ylim=(configurator["info"]["y_lim"][0], configurator["info"]["x_lim"][1]))

    ax, apartment = init_apartment(ax, configurator)
    #set_image_background()

    person = set_person_image()
    # person = plt.Circle((0, 0), 0.5, fc="b")
    time = plt.text(configurator["time"]["position"][0], configurator["time"]["position"][1], "",
                    fontsize=configurator["time"]["font_size"])
    sensor_output = plt.text(configurator["text_area_s"]["position"][0],
                             configurator["text_area_s"]["position"][1], "Sensors output",
                             fontsize=configurator["text_area_s"]["font_size"])

    if sys.argv[1] == "-f":
        df = utility.read_file(configurator["info"]["input_file"])
        prob = plt.text(configurator["text_area"]["position"][0],
                        configurator["text_area"]["position"][1], "", fontsize=configurator["text_area"]["font_size"])
        ev_level = plt.text(configurator["ev_level"]["position"][0], configurator["ev_level"]["position"][1], "",
                            fontsize=configurator["ev_level"]["font_size"])

        # filter_output = plt.Circle((0, 0), 2, fc='w', alpha=0.5)
        prob_value = set_prob_value()
        text_name = set_name()
        lines = set_line()
        df_filter = utility.read_file(configurator["info"]["evaluation_file"])
        step = len(configurator["probability_position"])+2
        gt_column_name = configurator["info"]["ground_truth_column_name"]
        ap_heat_map = set_apartment_heat_map()
        anim = animation.FuncAnimation(fig, animate_filter, init_func=init_filter, frames=len(df.index)-1,
                                       interval=configurator["info"]["time_speed"], blit=True, repeat=False)

    if sys.argv[1] == "-s":
        df = utility.read_file(configurator["info"]["input_file_s"])
        text_name = set_name()
        graph = set_background()
        lines = set_line()
        anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(df.index) - 1,
                                       interval=configurator["info"]["time_speed"], blit=True, repeat=False)

    # Writer = animation.writers['ffmpeg']
    # writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)
    # anim.save("graph_animation.mp4",writer=writer)
    plt.show()

