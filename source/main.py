import math
from cell import Cell
import sys
sys.path.append('../cell')
sys.path.append('../constants')

from lib import make_route
from lib import visualize_maze
from lib import read_file



if __name__ == "__main__":
    print("Hello, World!")
    bonus_points,  cellMatrix, beginCell, exitCell = read_file('input/level_2/example.txt')
    route = make_route(cellMatrix, beginCell, exitCell)

    visualize_maze(cellMatrix, bonus_points, [beginCell.row, beginCell.col], [exitCell.row, exitCell.col], route=route)
    