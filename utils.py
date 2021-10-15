class Vect2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

MAX_WIDTH_ROOM = 2
MAX_HEIGHT_ROOM = 2
MIN_WIDTH_ROOM = 2
MIN_HEIGHT_ROOM = 2

QTD_ROOMS = 8

PER_FLOOR = ([50, 100], 1)
PER_WALL = ([16, 49], 2)
PER_SPIKE = ([0, 15], 3)
