import utils as ut

import heapq as hp
import random as rand


class Finder:
    def __init__(self, start_x, start_y, final_x, final_y, graph):
        self.start = (start_x, start_y)
        self.finish = (final_x, final_y)
        print(self.start, self.finish)
        self.heap = []
        self.costs = [[-1 for _ in range(ut.COLUMNS)] for _ in range(ut.ROWS)]
        self.steps = self.dijkstras_finder(graph)

    def __find_possible_path(self, x, y, graph):
        possiblePath = []
        print(len(graph))
        print(x - 1 ,y)
        print(x + 1, y)
        print(x, y - 1)
        print(x, y + 1)
        if graph[x - 1][y][0] in [1, 2]: possiblePath.append((x - 1, y))
        if graph[x + 1][y][0] in [1, 2]: possiblePath.append((x + 1, y))
        if graph[x][y + 1][0] in [1, 2]: possiblePath.append((x, y + 1))
        if graph[x][y - 1][0] in [1, 2]: possiblePath.append((x, y - 1))
        return possiblePath

    def dijkstras_finder(self, graph):
        hp.heappush(self.heap, (0, self.start))
        self.costs[self.start[0]][self.start[1]] = 0
        path = [self.start]

        while self.heap:
            dist, cur_v = hp.heappop(self.heap)
            print(cur_v)
            graph[cur_v[0]][cur_v[1]][1] = True
            possible_path = self.__find_possible_path(cur_v[0], cur_v[1], graph)

            if cur_v == self.finish:
                return self.costs[cur_v[0]][cur_v[1]] + 1

            for n in possible_path:
                dist = graph[n[0]][n[1]][0]
                if not graph[n[0]][n[1]][1]:
                    o_cost = self.costs[n[0]][n[1]]
                    n_cost = self.costs[cur_v[0]][cur_v[1]] + dist
                    if n_cost < o_cost or o_cost == -1:
                        hp.heappush(self.heap, (n_cost, n))
                        self.costs[n[0]][n[1]] = n_cost
