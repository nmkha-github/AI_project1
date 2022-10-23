from lib import *
from search_algorithm.Heuristic import *
from search_algorithm.dfs import *
from search_algorithm.ucs import *
from search_algorithm.bfs import *
from search_algorithm.astar import *
from search_algorithm.gbfs import *
from search_algorithm.Heuristic import *
import os
from cell import *

if __name__ == "__main__":
    for filename in os.listdir('input/level_1/'):
        path = os.path.join('input/level_1/', filename)
        filenameTrip = filename.rsplit('.', 1)[0]
        os.makedirs(f'output/level_1/{filenameTrip}/')
        bonus_points,  cellMatrix, beginCell, exitCell = read_file(path)
        makeAdjList(cellMatrix)
        visitedOrder = []
        heuristicA = Heuristic(exitCell, 1)
        gbfs(beginCell, exitCell, visitedOrder, heuristicA)
        route = make_route(cellMatrix, beginCell, exitCell)
        out = f'output/level_1/{filenameTrip}/gbfs.jpg'
        visualize_maze(cellMatrix, bonus_points, [beginCell.row, beginCell.col], [
                       exitCell.row, exitCell.col], route=route, outputPath=out)
        f = open(f'output/level_1/{filenameTrip}/gbfs.txt', 'w')
        if exitCell.prev == None:
            f.write("NO")
        else:
            f.write(str(exitCell.distance))
