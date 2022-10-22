import math


class Cell:
    def __init__(self, row, col, cost) -> None:
        self.row = row
        self.col = col
        self.cost = cost
        self.distance = math.inf
        self.prev = None
        self.visited = False
        self.adj = []
        self.teleport = None
        self.f=-1

    def __str__(self) -> str:
        res = f'Pos: {self.row},{self.col}  Cost: {self.cost}  Dis: {self.distance}    ?{self.prev!=None}   Pre: '
        if self.prev is None:
            res = res + 'None'
        else:
            res = res + f'{self.prev.row},{self.prev.col}'
        return res

    def __lt__(self,other):
        return True