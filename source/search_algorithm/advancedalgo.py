from queue import Queue
import math
from queue import PriorityQueue


def advancedalgo(beginCell, exitCell, visitedOrder):
    if beginCell == exitCell:
        return
    open = PriorityQueue()
    beginCell.distance=0
    open.put((0, beginCell))
    while not open.empty():
        currentCell = open.get()[1]
        visitedOrder.append(currentCell)
        for nearCell in currentCell.adj:
            if nearCell == exitCell:
                nearCell.prev = currentCell
                if currentCell.teleport != None and nearCell.row == currentCell.teleport[0] and nearCell.col == currentCell.teleport[1]:
                    nearCell.distance = currentCell.distance
                else:
                    nearCell.distance = currentCell.distance + nearCell.cost
                visitedOrder.append(nearCell)
                return
            elif nearCell.prev == None:
                nearCell.prev = currentCell
                if currentCell.teleport != None and nearCell.row == currentCell.teleport[0] and nearCell.col ==  currentCell.teleport[1]:
                    nearCell.distance = currentCell.distance
                else:
                    nearCell.distance = currentCell.distance + nearCell.cost
                visitedOrder.append(nearCell)
                open.put((nearCell.distance, nearCell))