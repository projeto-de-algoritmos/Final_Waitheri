import utils as ut
import room as rm
import player as pl
import store as st
import quick_select as qs

import random as rand
from copy import deepcopy


class Game:
    def __init__(self, initial_status):
        self.game_status = initial_status
        self.opened_store = False
        self.store = st.Store((10, 20))
        self.size = ut.Vect2(ut.COLUMNS, ut.ROWS)
        self.graph = [[[0, False] for _ in range(self.size.x)] for _ in range(self.size.y)]
        self.rooms = self.__init_rooms()
        self.important_rooms = self.__find_rooms(0, 0, len(self.rooms)//2, len(self.rooms) - 1)
 
        self.__generate_middle_room()

        value = self.__generate_pos_in_room(0, 1)
        self.player = pl.Player(value[0], value[1])
        value = self.__generate_pos_in_room(2, 1)
        self.key = ut.Vect2(value[0], value[1])
        value = self.__generate_pos_in_room(1, 1)
        self.exit = ut.Vect2(value[0], value[1])

        self.player.calculate_steps(self.key, self.exit, deepcopy(self.graph))
        self.player.calculate_steps(self.player.pos, self.key, deepcopy(self.graph))

    def __init_rooms(self):
        rooms = []
        x_vec = [i for i in range(1, self.size.x - ut.MAX_WIDTH_ROOM - 1)]
        y_vec = [i for i in range(1, self.size.y - ut.MAX_HEIGHT_ROOM - 1)]
        rand.shuffle(x_vec)
        rand.shuffle(y_vec)

        def validate_x(value, x):
            if value + x > self.size.x - 1:
                return value - (value + x - self.size.x - 1)
            return value

        def validate_y(value, y):
            if value + y > self.size.y - 1:
                return value - (value + y - self.size.y - 1)
            return value

        for i in range(ut.QTD_ROOMS):
            room = rm.Room(
                x_vec[i],
                y_vec[i],
                validate_x(rand.randint(ut.MIN_WIDTH_ROOM, ut.MAX_WIDTH_ROOM), x_vec[i]),
                validate_y(rand.randint(ut.MIN_HEIGHT_ROOM, ut.MAX_HEIGHT_ROOM), y_vec[i])
            )
            
            room.init_nodes(self.graph)
            rooms.append(room)

        return rooms

    def __find_rooms(self, ordering, *args):
        important_rooms = []
        for value in args:
            qs.quickSelect(self.rooms, 0, len(self.rooms) - 1, value, ordering)
            important_rooms.append(self.rooms[value])

        return important_rooms

    def __generate_middle_room(self):
        important_rooms_y = self.__find_rooms(1, 0, 1, len(self.rooms) - 1)
        width = self.important_rooms[2].pos.x - self.important_rooms[0].pos.x
        height = important_rooms_y[2].pos.y - important_rooms_y[0].pos.y

        room = rm.Room(
            self.important_rooms[0].pos.x + self.important_rooms[0].size.x//2,
            important_rooms_y[0].pos.y + important_rooms_y[0].size.y//2,
            width, 
            height
        )
        room.init_nodes(self.graph)
        self.rooms.append(room)

    def __generate_pos_in_room(self, room, value):
        pos = (
            rand.randint(self.important_rooms[room].pos.x, self.important_rooms[room].pos.x + self.important_rooms[room].size.x - 2),
            rand.randint(self.important_rooms[room].pos.y, self.important_rooms[room].pos.y + self.important_rooms[room].size.y - 2)
        )

        self.graph[pos[1]][pos[0]][0] = value
        return pos
