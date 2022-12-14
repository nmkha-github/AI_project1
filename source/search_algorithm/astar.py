from queue import PriorityQueue
import os
import sys
sys.path.append(os.getcwd())


def astar(beginCell, exitCell, visitedOrder, heuristic):
    if beginCell == exitCell:
        return
    open = PriorityQueue()
    close = set()
    beginCell.f = 0+heuristic.getValue(beginCell)
    open.put((beginCell.f, beginCell))
    while not open.empty():
        currentCell = open.get()[1]
        visitedOrder.append(currentCell)
        close.add(currentCell)
        for nearCell in currentCell.adj:
            if nearCell == exitCell:
                nearCell.prev = currentCell
                nearCell.distance = currentCell.distance + nearCell.cost
                visitedOrder.append(nearCell)
                return
            elif nearCell not in close:
                gNew = currentCell.distance+nearCell.cost
                hNew = heuristic.getValue(nearCell)
                fNew = gNew+hNew
                if nearCell.f == -1 or nearCell.f > fNew:
                    nearCell.distance = gNew
                    nearCell.f = fNew
                    nearCell.prev = currentCell
                    nearCell.distance = currentCell.distance + nearCell.cost
                    open.put((fNew, nearCell))
