import sys
import matplotlib.pyplot as plt
from matplotlib import animation
import utility


def init_text(config):

    for state in config["state_position"]:
        plt.text(config["state_position"][state][0], config["state_position"][state][1], state, fontsize=12)


def found_state(row):
    for i in range(1, len(row)):
        if row[i] == 1:
            return str(i)


def update(conf, index):
    state = conf["index"][found_state(df.iloc[index])]
    fsm_state.set_color(conf["state_color"][state])
    fsm_state.center = conf["state_position"][state]


def init():
    update(configurator, 0)

    ax.add_patch(fsm_state)
    return fsm_state,


def animate(i):
    update(configurator, i)
    return fsm_state,


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Correct command = Animate_FSM.py name_of_the_configuration_file.json")
        sys.exit(1)

    configurator = utility.open_json(sys.argv[1])

    fig = plt.figure()
    fig.set_dpi(100)
    fig.set_size_inches(configurator["info"]["figure_size"][0], configurator["info"]["figure_size"][1])

    ax = plt.axes(xlim=(configurator["info"]["x_lim"][0], configurator["info"]["x_lim"][1]),
                  ylim=(configurator["info"]["y_lim"][0], configurator["info"]["x_lim"][1]))

    init_text(configurator)
    df = utility.read_file(configurator["info"]["input_file_Animate_FSM"])

    fsm_state = plt.Circle((2, 2), configurator["info"]["state_radius"], fc='b',  alpha=0.5)

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(df.index)-1,
                                   interval=configurator["info"]["time_speed"], blit=True, repeat=False)

    plt.show()

