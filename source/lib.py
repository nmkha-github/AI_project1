import math
import time
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

from cell import Cell


def read_file(file_name: str = 'maze.txt'):  # use for normal level (without teleport)
    f = open(file_name, 'r')
    n_bonus_points = int(next(f)[:-1])
    bonus_points = []
    for i in range(n_bonus_points):
        x, y, reward = map(int, next(f)[:-1].split(' '))
        bonus_points.append((x, y, reward))

    text = f.read()
    matrix = [list(i) for i in text.splitlines()]
    f.close()

    # make matrix of Cell
    cellMatrix = []
    beginCell = None
    exitCell = None
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            cost = (math.inf if matrix[i][j] == 'x' else 0)
            if (matrix[i][j] == '+'):
                for bonus_point in bonus_points:
                    if (bonus_point[0] == i and bonus_point[1] == j):
                        cost = bonus_point[2]
            cell = Cell(i, j, cost + 1)
            if ((matrix[i][j] == ' ') and (i == 0 or i == len(matrix) - 1 or j == 0 or j == len(matrix[i]) - 1)):
                exitCell = cell
            if (matrix[i][j] == 'S'):
                beginCell = cell
                beginCell.distance = 0
            row.append(cell)
        cellMatrix.append(row)

    return bonus_points, cellMatrix, beginCell, exitCell


# use for advanced level (with teleport)
def read_file_advance(file_name: str = 'maze.txt'):
    f = open(file_name, 'r')
    n_bonus_points = int(next(f)[:-1])
    bonus_points = []
    for i in range(n_bonus_points):
        x, y, reward = map(int, next(f)[:-1].split(' '))
        bonus_points.append((x, y, reward))

    n_door_pair = int(next(f)[:-1])
    teleport_pairs = []
    for i in range(n_door_pair):
        x1, y1, x2, y2 = map(int, next(f)[:-1].split(' '))
        teleport_pairs.append([x1, y1, x2, y2])

    text = f.read()
    matrix = [list(i) for i in text.splitlines()]
    f.close()

    # make matrix of Cell
    cellMatrix = []
    beginCell = None
    exitCell = None
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            cost = (math.inf if matrix[i][j] == 'x' else 0)
            if (matrix[i][j] == '+'):
                for bonus_point in bonus_points:
                    if (bonus_point[0] == i and bonus_point[1] == j):
                        cost = bonus_point[2]
            cell = Cell(i, j, cost + 1)
            if ((matrix[i][j] == ' ') and (i == 0 or i == len(matrix) - 1 or j == 0 or j == len(matrix[i]) - 1)):
                exitCell = cell
            if (matrix[i][j] == 'S'):
                beginCell = cell
                beginCell.distance = 0
            row.append(cell)
        cellMatrix.append(row)

    for teleport in teleport_pairs:
        cellMatrix[teleport[0]][teleport[1]].teleport = [
            teleport[2], teleport[3]]
        cellMatrix[teleport[2]][teleport[3]].teleport = [
            teleport[0], teleport[1]]

    return bonus_points, cellMatrix, beginCell, exitCell


def make_route(matrix, beginCell, exitCell):
    currentCell = exitCell
    if exitCell.prev == None:
        return []
    route = []
    while (currentCell != beginCell):
        # time.sleep(1)
        route.append([currentCell.row, currentCell.col])
        currentCell = currentCell.prev
    route.append([beginCell.row, beginCell.col])
    route.reverse()

    return route


def makeAdjList(cellMatrix):
    directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    for row in cellMatrix:
        for cell in row:
            for direction in directions:
                if 0 <= cell.row+direction[0] < len(cellMatrix) and 0 <= cell.col+direction[1] < len(cellMatrix[0]):
                    if cellMatrix[cell.row+direction[0]][cell.col+direction[1]].cost != math.inf:
                        cell.adj.append(
                            cellMatrix[cell.row+direction[0]][cell.col+direction[1]])
            if cell.teleport != None:
                cell.adj.append(cellMatrix[cell.teleport[0]][cell.teleport[1]])


def visualize_maze(matrix, bonus, start, end, outputPath, route=None, visited=None):
    """
    Args:
      1. matrix: The matrix read from the input file,
      2. bonus: The array of bonus points,
      3. start, end: The starting and ending points,
      4. route: The route from the starting point to the ending one, defined by an array of (x, y), e.g. route = [(1, 2), (1, 3), (1, 4)]
    """
    # 1. Define walls and array of direction based on the route
    walls = [(i, j) for i in range(len(matrix))
             for j in range(len(matrix[0])) if matrix[i][j].cost == math.inf]
    visited = [(i, j) for i in range(len(matrix))
               for j in range(len(matrix[0])) if matrix[i][j].prev]

    if route:
        direction = []
        for i in range(1, len(route)):
            if route[i][0]-route[i-1][0] > 0:
                direction.append('v')  # ^
            elif route[i][0]-route[i-1][0] < 0:
                direction.append('^')  # v
            elif route[i][1]-route[i-1][1] > 0:
                direction.append('>')
            else:
                direction.append('<')

        direction.pop(0)

    # 2. Drawing the map
    ax = plt.figure(
        figsize=(12, 12*len(matrix)/len(matrix[0])), dpi=100).add_subplot(111)

    for i in ['top', 'bottom', 'right', 'left']:
        ax.spines[i].set_visible(False)

    plt.scatter([i[1] for i in walls], [-i[0] for i in walls],
                marker='X', s=100, color='black')

    plt.scatter([i[1] for i in visited], [-i[0] for i in visited],
                marker='.', s=100, color='cornflowerblue')

    plt.scatter([i[1] for i in bonus], [-i[0] for i in bonus],
                marker='P', s=100, color='green')

    plt.scatter(start[1], -start[0], marker='*',
                s=100, color='gold')

    if route:
        for i in range(len(route)-2):
            plt.scatter(route[i+1][1], -route[i+1][0], s=80,
                        marker=direction[i], color='red')

    plt.text(end[1], -end[0], 'EXIT', color='red',
             horizontalalignment='center',
             verticalalignment='center')

    # draw teleports
    teleports = [matrix[i][j] for i in range(len(matrix)) for j in range(len(
        matrix[0])) if matrix[i][j].teleport != None]
    teleport_index = 1
    for teleport in teleports:
        plt.text(teleport.col, -teleport.row, teleport_index.__str__(), color='black',
                 horizontalalignment='center', fontweight='bold', backgroundcolor='gray',
                 verticalalignment='center')
        plt.text(teleport.teleport[1], -teleport.teleport[0], teleport_index.__str__(), color='black',
                 horizontalalignment='center', fontweight='bold', backgroundcolor='gray',
                 verticalalignment='center')
        teleport_index += 1
        teleports.remove(matrix[teleport.teleport[0]][teleport.teleport[1]])

    plt.xticks([])
    plt.yticks([])
    plt.savefig(outputPath)
    plt.show()
    print(f'Starting point (x, y) = {start[0], start[1]}')
    print(f'Ending point (x, y) = {end[0], end[1]}')

    for _, point in enumerate(bonus):
        print(
            f'Bonus point at position (x, y) = {point[0], point[1]} with point {point[2]}')
