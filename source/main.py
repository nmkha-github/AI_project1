from cell import Cell
from search_algorithm.bfs import *
from search_algorithm.Heuristic import *
from lib import *
from search_algorithm.dfs import *


if __name__ == "__main__":
    bonus_points,  cellMatrix, beginCell, exitCell = read_file(
        '../input/level_1/input1.txt')

    makeAdjList(cellMatrix)
    visitedOrder = []

    dfs(beginCell, exitCell, visitedOrder)
    route = make_route(cellMatrix, beginCell, exitCell)

    # print(visitedOrder)
    # print(route)

    visualize_maze(cellMatrix, bonus_points, [beginCell.row, beginCell.col], [
                   exitCell.row, exitCell.col], route=route)
