import utils as ut
import finder as fd

import random as rand


class Player:
    def __init__(self, x, y):
        self.pos = ut.Vect2(x, y)
        self.lifes = 3
        self.coins = 0
        self.remaining_steps = 0
        self.has_key = False

    def calculate_steps(self, start, finish, graph):
        finder = fd.Finder(start.x, start.y, finish.x, finish.y, graph)
        self.remaining_steps += finder.steps

    def __breack_box(self, graph, x, y):
        graph[y][x][0] = 1
        self.remaining_steps -= 1
        coin_per = rand.randint(1, 100)
        if coin_per <= ut.PER_COIN:
            graph[y][x][0] = 4

    def __pick_coin(self, graph, x, y):
        graph[y][x][0] = 1
        self.remaining_steps -= 1
        self.coins += 1

    def move_up(self, graph):
        if graph[self.pos.y - 1][self.pos.x][0] == 1:
            self.pos.y -= 1
            self.remaining_steps -= 1
        elif graph[self.pos.y - 1][self.pos.x][0] == 2:
            self.__breack_box(graph, self.pos.x, self.pos.y - 1)
        elif graph[self.pos.y - 1][self.pos.x][0] == 3:
            self.pos.y -= 1
            self.lifes -= 1
            self.remaining_steps -= 1
        elif graph[self.pos.y - 1][self.pos.x][0] == 4:
            self.__pick_coin(graph, self.pos.x, self.pos.y - 1)
            self.pos.y -= 1

        if self.remaining_steps < 0:
            self.lifes -= 1
            self.remaining_steps += 1

    def move_down(self, graph):
        if graph[self.pos.y + 1][self.pos.x][0] == 1:
            self.pos.y += 1
            self.remaining_steps -= 1
        elif graph[self.pos.y + 1][self.pos.x][0] == 2:
            self.__breack_box(graph, self.pos.x, self.pos.y + 1)
        elif graph[self.pos.y + 1][self.pos.x][0] == 3:
            self.pos.y += 1
            self.lifes -= 1
            self.remaining_steps -= 1
        elif graph[self.pos.y + 1][self.pos.x][0] == 4:
            self.__pick_coin(graph, self.pos.x, self.pos.y + 1)
            self.pos.y += 1

        if self.remaining_steps < 0:
            self.lifes -= 1
            self.remaining_steps += 1

    def move_left(self, graph):
        if graph[self.pos.y][self.pos.x - 1][0] == 1:
            self.pos.x -= 1
            self.remaining_steps -= 1
        elif graph[self.pos.y][self.pos.x - 1][0] == 2:
            self.__breack_box(graph, self.pos.x - 1, self.pos.y)
        elif graph[self.pos.y][self.pos.x - 1][0] == 3:
            self.pos.x -= 1
            self.lifes -= 1
            self.remaining_steps -= 1
        elif graph[self.pos.y][self.pos.x - 1][0] == 4:
            self.__pick_coin(graph, self.pos.x - 1, self.pos.y)
            self.pos.x -= 1

        if self.remaining_steps < 0:
            self.lifes -= 1
            self.remaining_steps += 1

    def move_right(self, graph):
        if graph[self.pos.y][self.pos.x + 1][0] == 1:
            self.pos.x += 1
            self.remaining_steps -= 1
        elif graph[self.pos.y][self.pos.x + 1][0] == 2:
            self.__breack_box(graph, self.pos.x + 1, self.pos.y)
        elif graph[self.pos.y][self.pos.x + 1][0] == 3:
            self.pos.x += 1
            self.lifes -= 1
            self.remaining_steps -= 1
        elif graph[self.pos.y][self.pos.x + 1][0] == 4:
            self.__pick_coin(graph, self.pos.x + 1, self.pos.y)
            self.pos.x += 1

        if self.remaining_steps < 0:
            self.lifes -= 1
            self.remaining_steps += 1
