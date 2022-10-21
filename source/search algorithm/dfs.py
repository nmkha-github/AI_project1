# todo: thêm hàm makeGraph biến đổi cellMatrix thành danh sách kề graph[]
def dfs(graph, beginCell, exitCell, bonus_points):
    route, stack = [], [beginCell]
    tracking = {beginCell: beginCell}

    while stack:
        currentCell = stack.pop()
        if currentCell == exitCell:
            break
        for neighbor in graph[currentCell]:
            if currentCell not in tracking:
                stack.append(neighbor)
                tracking[currentCell] = currentCell

 # backtrack ...

    return route
