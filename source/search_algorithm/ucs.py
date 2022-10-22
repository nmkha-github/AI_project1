

class Heap:
    def __init__(self):
        self.size = 0
        self.heap = [0]

    def empty(self):
        return self.size == 0

    def parent(self, pos):
        return pos//2

    def leftChild(self, pos):
        return 2 * pos

    def rightChild(self, pos):
        return (2 * pos) + 1

    def isLeaf(self, pos):
        return pos*2 > self.size

    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]

    def push(self, node):
        self.size += 1
        self.heap.append(node)
        current = self.size

        if self.size == 1:
            return

        while current > 0 and self.heap[current].distance < self.heap[self.parent(current)].distance:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def down(self, pos):
        m = self.leftChild(pos)
        if not self.isLeaf(pos):
            if self.heap[m].distance < self.heap[self.rightChild(pos)].distance:
                m = self.rightChild(pos)
            if self.heap[pos].distance > self.heap[m].distance:
                self.swap(self.heap[pos], self.heap[m])
                self.down(m)

    def pop(self):
        popped = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.down(1)
        return popped


def ucs(beginCell, exitCell, visitedOrder):
    heap = Heap()
    beginCell.distance = 0
    beginCell.prev = beginCell
    heap.push(beginCell)

    while not heap.empty():
        currentCell = heap.pop()
        print(currentCell, ' ')
        for x in heap.heap:
            if x == 0:
                continue
            print(x.row, x.col)
        visitedOrder.append(currentCell)

        if currentCell == exitCell:
            break

        for nearCell in currentCell.adj:
            if (nearCell.prev == None
                    and nearCell.distance > nearCell.cost + currentCell.distance):
                # print(currentCell.row, ',', currentCell.col,
                #       ' ', nearCell.row, ',', nearCell.col)
                nearCell.distance = nearCell.cost + currentCell.distance
                nearCell.prev = currentCell
                heap.push(nearCell)
