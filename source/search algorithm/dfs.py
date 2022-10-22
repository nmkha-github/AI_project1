# todo: thêm hàm makeGraph biến đổi cellMatrix thành danh sách kề graph[]
# todo: vehinh(begin,exit,matrixCell)
def dfs(adjList, beginCell, exitCell, visitedOrder):
    if beginCell == exitCell:
        return
    for neighbor in adjList[beginCell]:
        if neighbor.visited == False:
            neighbor.prev = beginCell
            neighbor.distance = beginCell.distance + neighbor.cost
            neighbor.visited = True
            visitedOrder.append(neighbor)
            dfs(adjList, neighbor, exitCell)
