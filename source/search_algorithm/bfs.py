from queue import Queue
import math


def bfs(beginCell, exitCell, visitedOrder):
    queue = Queue(0)
    queue.put(beginCell)
    while queue.empty() == False:
        current = queue.get()
        if current == exitCell:
            return
        for neighbor in current.adj:
            if neighbor.prev == None and neighbor.cost < math.inf:
                neighbor.prev = current
                neighbor.distance = current.distance + neighbor.cost
                neighbor.visited = True
                visitedOrder.append(neighbor)
                queue.put(neighbor)
