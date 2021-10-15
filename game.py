import utils as ut
import room as rm

import random as rand


class Game:
    def __init__(self):
        self.size = ut.Vect2(15, 13)
        self.graph = [[0 for _ in range(15)] for _ in range(13)]
        self.rooms = self.__init_rooms()

    def __init_rooms(self):
        rooms = []

        def validate_x(value, x):
            if value + x > 14:
                return value - (value + x - 14)
            return value

        def validate_y(value, y):
            if value + y > 12:
                return value - (value + y - 12)
            return value

        for i in range(ut.QTD_ROOMS):
            x = rand.randint(0, 11)
            y = rand.randint(0, 9)
            room = rm.Room(
                x,
                y,
                validate_x(rand.randint(ut.MIN_WIDTH_ROOM, ut.MAX_WIDTH_ROOM), x),
                validate_y(rand.randint(ut.MIN_HEIGHT_ROOM, ut.MAX_HEIGHT_ROOM), y)
            )
            
            room.init_nodes(self.graph)
            rooms.append(room)

        return rooms

g = Game()
for i in range(13):
    for j in range(15):
        print(g.graph[i][j], end=' ')
    print()
