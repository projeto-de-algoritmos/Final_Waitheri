import utils as ut

import heapq as hp
import random as rand


class Finder:
    def __init__(self, start_x, start_y, final_x, final_y, graph):
        self.start = (start_x, start_y)
        self.finish = (final_x, final_y)
        self.heap = []
        self.path = self.aStar_finder(graph)

    def __find_possible_path(self, x, y, graph):
        possiblePath = []
        if graph[x - 1][y][0] != 0 and not graph[x - 1][y][1]: possiblePath.append((x - 1, y))
        if graph[x + 1][y][0] != 0 and not graph[x + 1][y][1]: possiblePath.append((x + 1, y))
        if graph[x][y + 1][0] != 0 and not graph[x][y + 1][1]: possiblePath.append((x, y + 1))
        if graph[x][y - 1][0] != 0 and not graph[x][y - 1][1]: possiblePath.append((x, y - 1))
        return possiblePath

    def __calculate_distance(self, start_x, start_y, finish_x, finish_y):
        return (finish_x - start_x) ** 2 + (finish_y - start_y) ** 2

    def aStar_finder(self, graph):
        path = []
        # (F, (G, H), (start_x, start_y), (pai_x, pai_y))
        hp.heappush(self.heap, (0, (0, 0), self.start, self.start))

        while self.heap:
            print(self.heap)
            _, (G_C, _), (new_x, new_y), (cur_x, cur_y) = hp.heappop(self.heap)
            graph[new_x][new_y][1] = True
            path.insert(0, ((cur_x, cur_y), (new_x, new_y)))

            if (new_x, new_y) == self.finish:
                return path

            possible_path = self.__find_possible_path(new_x, new_y, graph)
            for n in possible_path:
                G = G_C + 1
                F = self.__calculate_distance(n[0], n[1], self.finish[0], self.finish[1])
                H = G + F * graph[n[0]][n[1]][0]
                hp.heappush(self.heap, (F, (G, H), n, (new_x, new_y)))



    # NÃO OLHAR OK
    #  def __find_neighbours(self, x, y, graph):
    #      def check_if_valid(x, y, direction):
    #          return x >= 0 and x < ut.COLUMNS and y >= 0 and y < ut.ROWS

    #      neighbours = []
    #      if check_if_valid(x, y + 1) and graph[x][y + 1][0] != 0: neighbours.append((x, y + 1))
    #      elif check_if_valid(x, y - 1) and graph[x][y - 1][0] != 0: neighbours.append((x, y - 1))
    #      elif check_if_valid(x + 1, y) and graph[x + 1][y][0] != 0: neighbours.append((x + 1, y))
    #      elif check_if_valid(x - 1, y) and graph[x - 1][y][0] != 0: neighbours.append((x - 1, y))
    #      rand.shuffle(neighbours)
    #      return neighbours

    #  def prim_finder(self, graph):
    #      hp.heappush(self.heap, (0, (self.x, self.y), (self.x, self.y)))

    #      while self.heap:
    #          _, (new_x, new_y), (cur_x, cur_y) = hp.heappop(self.heap)
    #          if not graph[new_x][new_y][1]:
    #              graph[new_x][new_y][1] = True
    #              neighbours = self.__find_neighbours(new_x, new_y)
    #              for n in neighbours:
    #                  if not graph[n[0]][n[1][1]:
    #                      hp.heappush(self.heap, (graph[n[0]][n[1][0], n, (new_x, new_y)))
