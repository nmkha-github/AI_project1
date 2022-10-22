import math


class Cell:
    def __init__(self, row, col, cost) -> None:
        self.row = row
        self.col = col
        self.cost = cost
        self.distance = math.inf
        self.visited = False
        self.prev = None
