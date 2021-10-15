import utils as ut
import room as rm
import quick_select as qs

import random as rand


class Game:
    def __init__(self):
        self.size = ut.Vect2(15, 13)
        self.graph = [[0 for _ in range(15)] for _ in range(13)]
        self.rooms = self.__init_rooms()
        self.important_rooms = self.find_rooms(0, 0, 1, len(self.rooms) - 1)

    def __init_rooms(self):
        rooms = []
        x_vec = [i for i in range(0, 12)]
        y_vec = [i for i in range(0, 10)]
        rand.shuffle(x_vec)
        rand.shuffle(y_vec)

        def validate_x(value, x):
            if value + x > 14:
                return value - (value + x - 14)
            return value

        def validate_y(value, y):
            if value + y > 12:
                return value - (value + y - 12)
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

    def find_rooms(self, ordering, *args):
        important_rooms = []
        for value in args:
            qs.quickSelect(self.rooms, 0, len(self.rooms) - 1, value, ordering)
            important_rooms.append(self.rooms[value])

        return important_rooms

g = Game()
print(g.important_rooms)
for i in range(13):
    for j in range(15):
        print(g.graph[i][j], end=' ')
    print()
