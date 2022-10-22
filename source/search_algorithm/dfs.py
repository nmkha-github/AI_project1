import math


def dfs(beginCell, exitCell, visitedOrder):
    if beginCell == exitCell:
        return -1
    for neighbor in beginCell.adj:
        if neighbor.prev == None:
            neighbor.prev = beginCell
            neighbor.distance = beginCell.distance + neighbor.cost
            neighbor.visited = True
            visitedOrder.append(neighbor)
            if dfs(neighbor, exitCell, visitedOrder) == -1:
                return -1
