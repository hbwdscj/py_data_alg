class Array(object):
    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size  # 给出长度为size，元素全为None的列表

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self, ):
        return len(self._items)

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self, ):
        for i in self._items:
            yield i


class MaxHeap(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception("Heap is full")
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count - 1)

    def _siftup(self, idx):  # 递归交换直到满足最大堆的特性
        if idx > 0:
            parent = int((idx - 1) / 2)
            if self._elements[idx] > self._elements[parent]:
                self._elements[idx], self._elements[parent] = self._elements[
                    parent], self._elements[idx]
                self._siftup(parent)

    def extract(self):
        if self._count <= 0:
            raise Exception("Heap is Empty")
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        self._siftdown(0)
        return value

    def _siftdown(self, idx):
        left = 2 * idx + 1
        right = 2 * idx + 2
        largest = idx

        if (left < self._count
                and self._elements[left] >= self._elements[largest]
                and self._elements[left] >= self._elements[right]):
            largest = left
        elif (right < self._count
              and self._elements[right] >= self._elements[largest]):
            largest = right

        if largest != idx:
            self._elements[idx], self._elements[largest] = self._elements[largest], self._elements[idx]
            self._siftdown(largest)


def test_max_heap():
    import random
    n = 5
    h = MaxHeap(n)
    for i in range(n):
        h.add(i)
    assert h.extract() == 4