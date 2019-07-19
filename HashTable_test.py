class Array(object):

    def __init__(self, size=32, init=None):
        self._size = size
        self._items = [init] * size  #给出长度为size，元素全为None的列表
    
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

class Slot(object):
    """
    定义一个 hash 表 数组的槽
    注意，一个槽有三种状态，看你能否想明白
    1.从未使用 HashMap.UNUSED。此槽没有被使用和冲突过，查找时只要找到 UNUSED 就不用再继续探查了
    2.使用过但是 remove 了，此时是 HashMap.EMPTY，该探查点后边的元素扔可能是有key
    3.槽正在使用 Slot 节点
    """
    def __init__(self, key, value):
        self.key, self.value = key, value

class HashTable(object):
   
    UNUSED = None   #slot未被使用过 
    EMPTY = Slot(None, None)    #slot使用过但被删除了  

    def __init__(self,):
        self._table = Array(8, init = HashTable.UNUSED)
        self.length = 0

    @property
    def _local_factor(self):
        return self.length / float(len(self._talble))

    def __len__(self):
        return len(self)

    def _hash(self, key):
        return abs(hash(key)) % len(self._table)

    def _find_key(self, key):
        index = self._hash(key)
        _len = len(self._table)
        while self._table[index] is not HashTable.UNUSED:
            if self._table[index] is HashTable.EMPTY:
                index = (index*5 + 1)%_len
                continue
            elif self._table[index].key == key:
                return index
            else:
                index = (index*5 +1 ) % _len
        return None

    def _slot_can_insert(self, index):
        return (self._table[index] is HashTable.EMPTY or HashTable.UNUSED)

    def _find_slot_for_insert(self, key):
        index = self._hash(key)    
        _len = len(self._table)
        while not self._slot_can_insert(index):
            index = (index*5 + 1) % _len
        return index

    def __contains__(self, key):     #in operator
        index = self._find_key(key)
        return (index is not None)
    
    def add(self, key, value):
        # key已经存在于原hashtable中，进行update操作并返回False
        if key in self:
            index = self._find_key(key)
            self._table[index].value = value
            return False
        else:
            index = self._find_slot_for_insert(key)
            self.table[index] = Slot(key ,value)
            self.length += 1
            if self._local_factor >= 0.8:
                self._rehash()  
            return True
    def _rehash(self,):
        old_table = self._table
        newsize = len(self._table) * 2
        self._table = Array(newsize, HashTable.UNUSED)
        self.length = 0 

        for slot in old_table:
            if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:
                index = self._find_slot_for_insert(slot.key)
                self._table[index] = slot
                self.length += 1
        
    def get(self, key, default=None):
        index = self._find_key(key)
        if index is None:
            return None
        return index

    def remove(self, key):
        index = self._find_key(key)
        if index is None:
            raise KeyError()
        value = self._table[index].value
        self.length -= 1    
        self._table[index] = HashTable.EMPTY
        return value

    def __iter__(self):
        # 遍历Key
        for slot in self._table:
            if slot not in (HashTable.UNUSED, HashTable.EMPTY):
                yield slot.key


def test_hash_table():
    h = HashTable()
    h.add('a', 0)
    h.add('b', 1)
    h.add('c', 2)
    assert len(h) == 3
    assert h.get('a') == 0
    assert h.get('b') == 1
    assert h.get('hehe') is None

    h.remove('a')
    assert h.get('a') is None
    assert sorted(list(h)) == ['b', 'c']

    n = 50
    for i in range(n):
        h.add(i, i)

    for i in range(n):
        assert h.get(i) == i

test_hash_table()
print(list(h))


