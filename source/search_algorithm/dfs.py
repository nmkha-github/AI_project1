import math

# todo: thêm hàm makeGraph biến đổi cellMatrix thành danh sách kề graph[]
# todo: vehinh(begin,exit,matrixCell)


def dfs(beginCell, exitCell, visitedOrder):
    if beginCell == exitCell:
        return
    for neighbor in beginCell.adj:
        if neighbor.prev == None and neighbor.cost < math.inf:
            neighbor.prev = beginCell
            neighbor.distance = beginCell.distance + neighbor.cost
            neighbor.visited = True
            visitedOrder.append(neighbor)
            dfs(neighbor, exitCell, visitedOrder)
