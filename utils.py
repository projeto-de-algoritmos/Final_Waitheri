class Vect2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

COLUMNS = 15
ROWS = 13

MAX_WIDTH_ROOM = 2
MAX_HEIGHT_ROOM = 2
MIN_WIDTH_ROOM = 2
MIN_HEIGHT_ROOM = 2

QTD_ROOMS = 8

PER_FLOOR = (100, 1)
PER_WALL = (49, 2)
PER_SPIKE = (7, 3)
