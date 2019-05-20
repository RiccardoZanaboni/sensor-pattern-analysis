
import random


class Human:
    """A class used to represent a person who lives in the apartment
            ...

            Attributes
            ------------------------
            current_room : Room
                the Room where the person is

            apartment : list of Room
                the Rooms by whom  the apartment is made up of

            time_next_move : int
                the time when the person will choose his next move

            model_movement : MotionDDP
                it's the ddp model from which the amount of waiting time in a room it's extracted

            Methods
            -----------------------

            alert_sensor(self, current_time, human)
                simulate the sensor's behaviour

            """

    def __init__(self, apartment, model_movement):
        self.current_room = 0
        self.apartment = apartment
        self.time_next_move = 0                 # has to be synchronised to the system clock
        self.model_movement = model_movement

    @property
    def current_room(self):
        return self.__current_room

    @current_room.setter
    def current_room(self, current_room):
        self.__current_room = current_room

    @property
    def apartment(self):
        return self.__apartment

    @apartment.setter
    def apartment(self, apartment):
        self.__apartment = apartment

    @property
    def time_next_move(self):
        return self.__time_next_move

    @time_next_move.setter
    def time_next_move(self, time_next_move):
        self.__time_next_move = time_next_move

    @property
    def model_movement(self):
        return self.__model_movement

    @model_movement.setter
    def model_movement(self, model_movement):
        self.__model_movement = model_movement

    def move(self, current_time):
        """
        make the person moves , by choosing randomly between one of the current room 's adjacencies

        :param current_time: int
                the timer of the system
        :return: int
            the time when the person will choose his next move

        """
        self.current_room = random.choice(self.current_room.adjacencies)

        def stay():
            """
            simulate for how long the person stay in the current room
            :return: int
                the time at which the person will choose his next move
            """
            nonlocal current_time
            tmp = self.model_movement.generate_random_time()
            print("h" + str(tmp))
            return current_time + tmp

        self.time_next_move = stay()

    def chose_start_room(self):
        """
        initialize the room where the person starts the simulation
        :return:

        """
        self.current_room = random.choice(self.apartment)


