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
        return self.length / float(len(self._table))

    def __len__(self):
        return self.length

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


    def _find_slot_for_insert(self, key):
        index = self._hash(key)    
        _len = len(self._table)
        while not self._slot_can_insert(index):
            index = (index*5 + 1) % _len
        return index

    def _slot_can_insert(self, index):
        return (self._table[index] is HashTable.EMPTY or self._table[index] is HashTable.UNUSED)

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
            self._table[index] = Slot(key ,value)
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
            return default
        else:   
            return self._table[index].value
            
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

###########################
#以下为dict实现 
###########################
class DictADT(HashTable):
    def __setitem__(self, key, value):  
        self.add(key, value)

    def __getitem__(self, key):
        if key not in self:
            raise KeyError()
        else:
            return self.get(key)

    def _iter_slot(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot

    def items(self):
        for slot in self._iter_slot():
            yield (slot.key, slot.value)
        
    def keys(self):
        for slot in self._iter_slot():
            yield (slot.key)

    def values(self):
        for slot in self._iter_slot():
            yield (slot.value)

def test_dictadt():
    import random
    d = DictADT()

    d['a'] = 1
    assert d['a'] == 1
    d.remove('a')

    l = list(range(30))
    random.shuffle(l)
    for i in l:
        d.add(i, i)
    
    for i in range(30):
        assert d.get(i) == i

    assert sorted(list(d.keys())) == sorted(l)

