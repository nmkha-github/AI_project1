import math

class Cell:
    def __init__(self, row, col, cost) -> None:
        self.row = row
        self.col = col
        self.cost = cost
        self.distance = float(math.inf)
        self.visited = False
        self.previous = None
    def __eq__(self, other: object) -> bool:
        return self.col == other.col and self.row == other.row
    def __str__(self) -> str:
        res =  f'Pos: {self.row},{self.col}  Cost: {self.cost}  Dis: {self.distance}    ?{self.visited}   Pre: '
        if self.previous is None:
            res = res + 'None'
        else:
            res = res + f'{self.previous.row},{self.previous.col}'
        return res

        
