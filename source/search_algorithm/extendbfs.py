from queue import Queue
import math


def extendbfs(beginCell, exitCell, visitedOrder):
    queue = Queue(0)
    queue.put(beginCell)
    while queue.empty() == False:
        current = queue.get()
        if current == exitCell:
            return
        for neighbor in current.adj:
            if neighbor.prev == None:
                neighbor.prev = current
                if neighbor.teleport!=None and neighbor.row==neighbor.teleport[0] and neighbor.col==neighbor.teleport[1]:
                    neighbor.distance = current.distance
                else:
                    neighbor.distance = current.distance + neighbor.cost
                neighbor.visited = True
                visitedOrder.append(neighbor)
                queue.put(neighbor)
