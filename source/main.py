from lib import *
from search_algorithm.Heuristic import *
from search_algorithm.dfs import *
from search_algorithm.ucs import *
from search_algorithm.bfs import *
from search_algorithm.extendbfs import *
from search_algorithm.algo1 import *
from search_algorithm.astar import *
from search_algorithm.gbfs import *
from search_algorithm.Heuristic import *
import os
from cell import *

if __name__ == "__main__":
    print("level_1")
    for filename in os.listdir('input/level_1/'):
        path = os.path.join('input/level_1/', filename)
        filenameTrip = filename.rsplit('.', 1)[0]
        print(filenameTrip)
        os.makedirs(f'output/level_1/{filenameTrip}')
        bonus_points,  cellMatrix, beginCell, exitCell = read_file(path)
        makeAdjList(cellMatrix)
        heuristicA = Heuristic(exitCell, 1)
        heuristicB = Heuristic(exitCell, 2)
        'DFS'
        resetMatrix(cellMatrix, beginCell)
        visitedOrder = []
        dfs(beginCell, exitCell, visitedOrder)
        route = make_route(cellMatrix, beginCell, exitCell)
        out = f'output/level_1/{filenameTrip}/dfs.jpg'
        visualize_maze(cellMatrix, bonus_points, [beginCell.row, beginCell.col], [
                       exitCell.row, exitCell.col], route=route, outputPath=out)
        f = open(f'output/level_1/{filenameTrip}/dfs.txt', 'w')
        if exitCell.prev == None:
            f.write("NO")
        else:
            f.write(str(exitCell.distance))
        'BFS'
        resetMatrix(cellMatrix, beginCell)
        visitedOrder = []
        bfs(beginCell, exitCell, visitedOrder)
        route = make_route(cellMatrix, beginCell, exitCell)
        out = f'output/level_1/{filenameTrip}/bfs.jpg'
        visualize_maze(cellMatrix, bonus_points, [beginCell.row, beginCell.col], [
                       exitCell.row, exitCell.col], route=route, outputPath=out)
        f = open(f'output/level_1/{filenameTrip}/bfs.txt', 'w')
        if exitCell.prev == None:
            f.write("NO")
        else:
            f.write(str(exitCell.distance))
        'UCS'
        resetMatrix(cellMatrix, beginCell)
        visitedOrder = []
        ucs(beginCell, exitCell, visitedOrder)
        route = make_route(cellMatrix, beginCell, exitCell)
        out = f'output/level_1/{filenameTrip}/ucs.jpg'
        visualize_maze(cellMatrix, bonus_points, [beginCell.row, beginCell.col], [
                       exitCell.row, exitCell.col], route=route, outputPath=out)
        f = open(f'output/level_1/{filenameTrip}/ucs.txt', 'w')
        if exitCell.prev == None:
            f.write("NO")
        else:
            f.write(str(exitCell.distance))
        'GBFS heuristic A'
        resetMatrix(cellMatrix, beginCell)
        visitedOrder = []
        gbfs(beginCell, exitCell, visitedOrder, heuristicA)
        route = make_route(cellMatrix, beginCell, exitCell)
        out = f'output/level_1/{filenameTrip}/gbfsA.jpg'
        visualize_maze(cellMatrix, bonus_points, [beginCell.row, beginCell.col], [
                       exitCell.row, exitCell.col], route=route, outputPath=out)
        f = open(f'output/level_1/{filenameTrip}/gbfsA.txt', 'w')
        if exitCell.prev == None:
            f.write("NO")
        else:
            f.write(str(exitCell.distance))
        'GBFS heuristic B'
        resetMatrix(cellMatrix, beginCell)
        visitedOrder = []
        gbfs(beginCell, exitCell, visitedOrder, heuristicB)
        route = make_route(cellMatrix, beginCell, exitCell)
        out = f'output/level_1/{filenameTrip}/gbfsB.jpg'
        visualize_maze(cellMatrix, bonus_points, [beginCell.row, beginCell.col], [
            exitCell.row, exitCell.col], route=route, outputPath=out)
        f = open(f'output/level_1/{filenameTrip}/gbfsB.txt', 'w')
        if exitCell.prev == None:
            f.write("NO")
        else:
            f.write(str(exitCell.distance))
        'A* heuristic A'
        resetMatrix(cellMatrix, beginCell)
        visitedOrder = []
        astar(beginCell, exitCell, visitedOrder, heuristicA)
        route = make_route(cellMatrix, beginCell, exitCell)
        out = f'output/level_1/{filenameTrip}/astarA.jpg'
        visualize_maze(cellMatrix, bonus_points, [beginCell.row, beginCell.col], [
            exitCell.row, exitCell.col], route=route, outputPath=out)
        f = open(f'output/level_1/{filenameTrip}/astarA.txt', 'w')
        if exitCell.prev == None:
            f.write("NO")
        else:
            f.write(str(exitCell.distance))
        'A* heuristic B'
        resetMatrix(cellMatrix, beginCell)
        visitedOrder = []
        astar(beginCell, exitCell, visitedOrder, heuristicB)
        route = make_route(cellMatrix, beginCell, exitCell)
        out = f'output/level_1/{filenameTrip}/astarB.jpg'
        visualize_maze(cellMatrix, bonus_points, [beginCell.row, beginCell.col], [
            exitCell.row, exitCell.col], route=route, outputPath=out)
        f = open(f'output/level_1/{filenameTrip}/astarB.txt', 'w')
        if exitCell.prev == None:
            f.write("NO")
        else:
            f.write(str(exitCell.distance))

    print("level_2")
    for filename in os.listdir('input/level_2/'):
        path = os.path.join('input/level_2/', filename)
        filenameTrip = filename.rsplit('.', 1)[0]
        os.makedirs(f'output/level_2/{filenameTrip}')
        bonus_points,  cellMatrix, beginCell, exitCell = read_file(path)
        makeAdjList(cellMatrix)
        visitedOrder = []
        route, distance = algo1(cellMatrix, beginCell, exitCell, bonus_points)
        out = f'output/level_2/{filenameTrip}/algo1.jpg'
        visualize_maze(cellMatrix, bonus_points, [beginCell.row, beginCell.col], [
                       exitCell.row, exitCell.col], route=route, outputPath=out)
        f = open(f'output/level_2/{filenameTrip}/algo1.txt', 'w')
        if exitCell.prev == None:
            f.write("NO")
        else:
            f.write(str(distance))


    print("level_advance")
    for filename in os.listdir('input/advance/'):
        path = os.path.join('input/advance/', filename)
        filenameTrip = filename.rsplit('.', 1)[0]
        os.makedirs(f'output/advance/{filenameTrip}')

        bonus_points, cellMatrix, beginCell, exitCell = read_file_advance(path)
        makeAdjList(cellMatrix)
        visitedOrder = []
        extendbfs(beginCell, exitCell, visitedOrder)
        route = make_route(cellMatrix, beginCell, exitCell)

        out = f'output/advance/{filenameTrip}/extendbfs.jpg'
        visualize_maze(cellMatrix, bonus_points, [beginCell.row, beginCell.col], [
            exitCell.row, exitCell.col], route=route, outputPath=out)
        f = open(f'output/advance/{filenameTrip}/extendbfs.txt', 'w')

        if exitCell.prev == None:
            f.write("NO")
        else:
            f.write(str(exitCell.distance))
