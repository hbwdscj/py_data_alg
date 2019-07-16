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

class FullError(Exception):
    pass

class ArrayQueue(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.array = Array(maxsize) 
        self.head = 0   # 首值  
        self.tail = 0   # 尾值
    def __len__(self):
        return self.head - self.tail
    def push(self, value):
        if len(self) >= self.maxsize:
            raise FullError('Queue is full')
        self.array[self.head % self.maxsize] = value      # 详解见笔记本
        self.head += 1
    
    def pop(self):
        value = self.array[self.tail % self.maxsize]
        self.tail += 1
        return value

def test_array_queue():
    import pytest
    size = 5
    q = ArrayQueue(size)
    for i in range(size):
        q.push(i)

    with pytest.raises(FullError) as excinfo:
        q.push(size)
    assert 'full' in str(excinfo.value)

    assert len(q) == size

    assert q.pop() == 0 
    assert q.pop() == 1

    q.push(5)
    assert len(q) == 4
     
    assert q.pop() == 2
    assert q.pop() == 3
    assert q.pop() == 4
    assert q.pop() == 5

    assert len(q) == 0
