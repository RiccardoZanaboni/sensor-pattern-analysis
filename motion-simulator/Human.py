import random
import numpy as np


class Human:
    """Person who lives in the apartment
            ...

            Attributes
            ------------------------
            current_room : Room
                the Room where the person is

            apartment : list of Room
                the Rooms by whom  the apartment is made up of

            time_next_move : int
                the time when the person will choose his next move

            short_time_model_movement : UniformDDP
                it's the ddp model from which the amount of short waiting time in a room it's extracted

            long_time_model_movement : UniformDDP
                it's the ddp model from which the amount of long waiting time in a room it's extracted



            p_of_staying : float
                probability of staying in the room

            p_type_behaviour : float
                probability on which is selected the model for the time permanence in the room

            Methods
            -----------------------

            alert_sensor(self, current_time, human)
                simulate the sensor's behaviour

            """

    def __init__(self, apartment, model_movement):
        self.current_room = 0
        self.apartment = apartment
        self.time_next_move = 0                 # has to be synchronised to the system clock
        self.long_time_model_movement = model_movement[0]
        self.p_of_staying = 0
        self.p_type_behaviour = 0
        self.short_time_model_movement = model_movement[1]


    @property
    def p_of_staying(self):
        return self.__p_of_staying

    @p_of_staying.setter
    def p_of_staying(self, p_of_staying):
        self.__p_of_staying = p_of_staying

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
    def long_time_model_movement(self):
        return self.__long_time_model_movement

    @long_time_model_movement.setter
    def long_time_model_movement(self, model_movement):
        self.__long_time_model_movement = model_movement
    @property
    def short_time_model_movement(self):
        return self.__short_time_model_movement

    @short_time_model_movement.setter
    def short_time_model_movement(self, model_movement):
        self.__short_time_model_movement = model_movement

    def move(self, current_time):
        """
        make the person moves , by choosing randomly between one of the current room 's adjacencies

        :param current_time: int
                the timer of the system
        :return: int
            the time when the person will choose his next move

        """
        self.current_room = random.choice(self.current_room.adjacencies)

        def stay(p_of_staying, p_type_behaviour):
            """
            simulate for how long the person stay in the current room
            :return: int
                the time at which the person will choose his next move
            """
            nonlocal current_time
            if np.random.uniform(0, 1) > p_of_staying:
                tmp = 1
            else:
                # tmp = random.choice([self.long_time_model_movement, self
                #                      .short_time_model_movement])
                # tmp = tmp.generate_random_time()
                if np.random.uniform(0, 1) > p_type_behaviour:
                    tmp = self.long_time_model_movement.generate_random_time()
                else:
                    tmp = self.short_time_model_movement.generate_random_time()

            return current_time + tmp

        self.time_next_move = stay(self.p_of_staying, self.p_type_behaviour)

    def chose_start_room(self, p_of_staying, p_type_behaviour):
        """
        initialize the room where the person starts the simulation and set the probability of staying
        :return:

        """
        self.current_room = random.choice(self.apartment)
        self.time_next_move = self.short_time_model_movement.generate_random_time()
        self.p_of_staying = p_of_staying
        self.p_type_behaviour = p_type_behaviour
