import utils as ut

import random as rand


class Room:
    def __init__(self, x, y, width, height):
        self.pos = ut.Vect2(x, y)
        self.size = ut.Vect2(width, height)

    def __repr__(self):
        return f'{self.pos.x}, {self.pos.y}, {self.size.x}, {self.size.y}'

    def init_nodes(self, graph):
        for i in range(self.pos.x, self.pos.x + self.size.x + 1):
            for j in range(self.pos.y, self.pos.y + self.size.y + 1):
                if graph[j][i] != 0:
                    continue

                value = rand.randint(0, 100)
                if value in range(ut.PER_WALL[0] + 1, ut.PER_FLOOR[0] + 1):
                    graph[j][i] = ut.PER_FLOOR[1]
                elif value in range(ut.PER_SPIKE[0] + 1, ut.PER_WALL[0] + 1):
                    graph[j][i] = ut.PER_WALL[1]
                else:
                    graph[j][i] = ut.PER_SPIKE[1]
