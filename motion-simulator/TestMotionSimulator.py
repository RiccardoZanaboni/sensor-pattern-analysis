# Motion Simulator : simulate human's movement in an apartment from START_TIME to STOP_TIME

# json / toml
import Room as room
import Human as human
import pandas as pd
import Simulate_Time as st
import MotionNormalDDP as model


def create_apartment():
    apartment = []
    kitchen = room.Room("Kitchen",0)
    apartment.append(kitchen)
    atrium1 = room.Room("Atrium1",0)
    apartment.append(atrium1)
    atrium2 = room.Room("Atrium2",0)
    apartment.append(atrium2)
    livingroom1 = room.Room("Livingroom1",0)
    apartment.append(livingroom1)
    livingroom2 = room.Room("Livingroom2",0)
    apartment.append(livingroom2)
    dinneroom = room.Room("Dinneroom",0)
    apartment.append(dinneroom)
    toilet = room.Room("Toilet",0)
    apartment.append(toilet)
    bedroom = room.Room("Bedroom",0)
    apartment.append(bedroom)
    corridor = room.Room("Corridor",0)
    apartment.append(corridor)

    kitchen.adjacencies = [atrium1]
    atrium1.adjacencies = [kitchen, corridor, livingroom1, atrium2]
    atrium2.adjacencies = [atrium1, dinneroom, livingroom2]
    livingroom1.adjacencies = [atrium1, livingroom2]
    livingroom2.adjacencies = [atrium2, livingroom1]
    dinneroom.adjacencies = [atrium2, corridor]
    toilet.adjacencies = [corridor]
    bedroom.adjacencies = [corridor]
    corridor.adjacencies = [toilet, bedroom, atrium1, dinneroom]

    return apartment


if __name__ == "__main__":

    START_TIME = 0
    STOP_TIME = 10000
    current_time = START_TIME
    apartment = create_apartment()
    movement_tracker = pd.DataFrame(columns=['Time', 'Room'])
    normal_model = model.MotionNormalDDP()
    mat = human.Human(apartment, normal_model)
    mat.chose_start_room()
    movement_tracker = movement_tracker.append({'Time': current_time, 'Room': mat.current_room.name}, ignore_index=True)
    current_time = st.increase_time(current_time)
    mat.time_next_move = current_time               # synchronisation of human's timer to the system clock

    while current_time < STOP_TIME:

        if current_time == mat.time_next_move:
            mat.move(current_time)                          # if timer is equal to human's timer-decision : human moves
            movement_tracker = movement_tracker.append({'Time': current_time, 'Room': mat.current_room.name},
                                                       ignore_index=True)
        current_time = st.increase_time(current_time)

    movement_tracker.to_csv("out.csv", index=False)




