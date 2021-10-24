import utils as ut

import heapq as hp
import random as rand


class Finder:
    def __init__(self, start_x, start_y, final_x, final_y, graph):
        self.start = (start_x, start_y)
        self.finish = (final_x, final_y)
        self.heap = []
        self.costs = [[-1 for _ in range(ut.COLUMNS)] for _ in range(ut.ROWS)]
        self.steps = self.dijkstras_finder(graph)

    def find_possible_path(self, y, x, graph):
        possiblePath = []
        if graph[x - 1][y][0] in [1, 2]: possiblePath.append((x - 1, y))
        if graph[x + 1][y][0] in [1, 2]: possiblePath.append((x + 1, y))
        if graph[x][y + 1][0] in [1, 2]: possiblePath.append((x, y + 1))
        if graph[x][y - 1][0] in [1, 2]: possiblePath.append((x, y - 1))
        return possiblePath

    def dijkstras_finder(self, graph):
        hp.heappush(self.heap, (0, self.start))
        self.costs[self.start[1]][self.start[0]] = 0

        while self.heap:
            _, cur_v = hp.heappop(self.heap)

            possible_path = self.find_possible_path(cur_v[0], cur_v[1], graph)
            graph[cur_v[1]][cur_v[0]][1] = True

            for n in possible_path:
                if not graph[n[0]][n[1]][1]:
                    dist = graph[n[0]][n[1]][0]
                    o_cost = self.costs[n[0]][n[1]]
                    n_cost = self.costs[cur_v[1]][cur_v[0]] + dist
                    if n_cost < o_cost or o_cost == -1:
                        hp.heappush(self.heap, (n_cost, (n[1], n[0])))
                        self.costs[n[0]][n[1]] = n_cost

        return self.costs[self.finish[1]][self.finish[0]]
