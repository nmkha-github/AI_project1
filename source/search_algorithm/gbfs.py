import os
import sys
sys.path.append(os.getcwd())
from typing import Any
from queue import PriorityQueue
from .Heuristic import *
def gbfs(beginCell, exitCell,visitedOrder,type):
    if beginCell==exitCell:
        return
    open=PriorityQueue()
    heuristic=Heuristic(exitCell,type)
    beginCell.f=heuristic.getValue(beginCell)
    open.put((beginCell.f,beginCell))
    while not open.empty():
        currentCell = open.get()[1]
        visitedOrder.append(currentCell)
        for nearCell in currentCell.adj:
            if nearCell==exitCell:
                nearCell.prev = currentCell
                visitedOrder.append(nearCell)
                return
            elif nearCell.prev==None:
                nearCell.prev=currentCell
                nearCell.f=heuristic.getValue(nearCell)
                open.put((nearCell.f,nearCell))



