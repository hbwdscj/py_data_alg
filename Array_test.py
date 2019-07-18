class Array(object):
    def __init__(self, size=32):
        self._size = size
        self._items = [None] * size  #给出长度为size，元素全为None的列表
    
    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self,):
        return len(self._items)
    
    def clear (self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self,):
        for i in self._items:
            yield i

def test_array():
    size = 10
    a = Array(size)
    a[0] = 1
    assert a[0] == 1
    a.clear()
    assert a[0] is None