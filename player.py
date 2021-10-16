import utils as ut


class Player:
    def __init__(self, x, y):
        self.pos = ut.Vect2(x, y)
        self.lifes = 3
        self.remaining_steps = 0
        self.has_key = False
