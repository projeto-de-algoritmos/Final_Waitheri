import utils as ut
import finder as fd


class Player:
    def __init__(self, x, y):
        self.pos = ut.Vect2(x, y)
        self.lifes = 3
        self.remaining_steps = 0
        self.has_key = False

    def calculate_steps(self, start, finish, graph):
        finder = fd.Finder(start.x, start.y, finish.x, finish.y, graph.copy())
        print(finder.path)
        print(len(finder.path))
