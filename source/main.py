from lib import *
from search_algorithm.Heuristic import *
from search_algorithm.dfs import *
from search_algorithm.ucs import *
from search_algorithm.bfs import *
from search_algorithm.astar import *
from search_algorithm.gbfs import *
from search_algorithm.Heuristic import *
from cell import *

if __name__ == "__main__":
    bonus_points,  cellMatrix, beginCell, exitCell = read_file(
        '../input/level_1/input1.txt')

    makeAdjList(cellMatrix)
    visitedOrder = []
    heuristicA=Heuristic(exitCell,1)
    gbfs(beginCell, exitCell, visitedOrder,heuristicA)
    route = make_route(cellMatrix, beginCell, exitCell)

    visualize_maze(cellMatrix, bonus_points, [beginCell.row, beginCell.col], [
                   exitCell.row, exitCell.col], route=route)
