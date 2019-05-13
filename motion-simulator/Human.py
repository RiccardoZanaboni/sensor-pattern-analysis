
import random


class Human:

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
    def model_movement(self,model_movement):
        self.__model_movement = model_movement

    def move(self, current_time):
        self.current_room = random.choice(self.current_room.adjacencies)

        def stay():
            nonlocal current_time

            return current_time + self.model_movement.generate_waiting_time()

        self.time_next_move = stay()

    def chose_start_room(self):
        self.current_room = random.choice(self.apartment)


