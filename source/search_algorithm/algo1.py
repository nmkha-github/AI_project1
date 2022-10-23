

from source.search_algorithm.ucs import *


def findNearestCellCanExit(cell, route):
    distance = 0
    tempRoute = []
    currentCell = cell
    while not currentCell.canExit:
        tempRoute.append(currentCell)
        distance += currentCell.cost
        currentCell.canExit = True
        currentCell = currentCell.prev

    temp1 = []
    for r in tempRoute:
        temp1.append([r.row, r.col])
    temp1.append([currentCell.row, currentCell.col])

    tempRoute.reverse()
    temp2 = []
    for r in tempRoute:
        temp2.append([r.row, r.col])
    temp2 = temp2[:-1]

    sumRoute = temp2 + temp1
    if (distance - cell.cost) * 2 + cell.cost < 0:
        pos = route.index([currentCell.row, currentCell.col]) + 1
        route[pos:pos] = sumRoute


def algo1(cellMatrix, beginCell, exitCell, bonus_points):
    visitedOrder = []
    ucs(beginCell, exitCell, visitedOrder, findAll=True)

    currentCell = exitCell
    if exitCell.prev == None:
        return []

    route = []
    while (currentCell != beginCell):
        route.append([currentCell.row, currentCell.col])
        currentCell.canExit = True
        currentCell = currentCell.prev

    route.append([beginCell.row, beginCell.col])
    route.reverse()

    for bonus in bonus_points:
        if not currentCell.canExit:
            bonusCell = cellMatrix[bonus[0]][bonus[1]]
            findNearestCellCanExit(bonusCell, route)

    totalDistance = 0
    for point in route[1:]:
        totalDistance += cellMatrix[point[0]][point[1]].cost
        if cellMatrix[point[0]][point[1]].cost <= 0:
            cellMatrix[point[0]][point[1]].cost = 1

    return route, totalDistance
