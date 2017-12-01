class Heap(object):
    def __init__(self, lst):
        self.heap = []
        if lst:
            self.build_max_heap(lst)

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def parent(self, i):
        if i == 0:
            return -1
        elif i % 2 != 0:
            return (i - 1) // 2
        else:
            return (i - 2) // 2

    def heap_size(self):
        return len(self.heap)

    def swap(self, x, y):
        temp = self.heap[x]
        self.heap[x] = self.heap[y]
        self.heap[y] = temp

    def insert(self, x):
        self.heap.append(x)

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        largest = i
        if l < self.heap_size() and self.heap[l] > self.heap[largest]:
            largest = l
        if r < self.heap_size() and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.swap(i, largest)
            self.max_heapify(largest)

    def build_max_heap(self, lst):
        self.heap = lst[:]
        leaf = self.parent(self.heap_size())
        for i in range(leaf, -1, -1):
            self.max_heapify(i)

    def heap_sort(self):
        end = self.heap_size() - 1
        temp = []
        while self.heap_size():
            self.swap(0, end)
            end -= 1
            pop = self.heap.pop()
            temp.append(pop)
            self.max_heapify(0)
        self.heap = temp[:]


if __name__ == "__main__":
    x = [16, 14, 10, 12, 11, 4, 2, 5, 3, 6]
    h = Heap(x)
    print(h.heap)
    h.insert(15)
    print(h.heap)
    h.heap_sort()
    print(h.heap)
