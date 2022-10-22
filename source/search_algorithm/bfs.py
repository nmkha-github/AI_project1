from queue import Queue
import math

def bfs(beginCell, exitCell, visitedOrder):
    if beginCell == exitCell:
        return
    queue = Queue(0)
    queue.put(beginCell)
    while not queue.empty():
        current=queue.get()
        for neighbor in current.adj:
            if neighbor.prev == None and neighbor.cost < math.inf:
                neighbor.prev = current
                neighbor.distance = current.distance + neighbor.cost
                neighbor.visited = True
                visitedOrder.append(neighbor)
                queue.put(neighbor)
