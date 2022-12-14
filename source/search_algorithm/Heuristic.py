import os, sys

parent = os.path.abspath('.')
sys.path.insert(1, parent)

from cell import Cell
import math

class Heuristic:
    TYPE_MANHATTAN_DISTANCE = 1

    def __init__(self, exitCell, type) -> None:
        self.exitCell = exitCell
        self.type = type

    def getValue(self, cell):
        if self.type == self.TYPE_MANHATTAN_DISTANCE:
            return self._heuristic1(cell)
        elif self.type == 2:
            return self._heuristic2(cell)
        else:
            return 0

    def _heuristic1(self, cell):
        return abs(cell.row - self.exitCell.row) + abs(cell.col - self.exitCell.col)

    def _heuristic2(self, cell):
        return math.sqrt((cell.row-self.exitCell.row)**2+(cell.col+self.exitCell.col)**2)
