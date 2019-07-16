class Node(object):
    def __init__(self, value=None, next=None):
        self.value, self.next = value, next


class Linkedlist(object):
    def __init__(self, maxsize=None ):  # maxsize为None说明长度无限
        self.maxsize = maxsize
        self.root = Node()
        self.length = 0
        self.tailnode = None  # 尾节点

    def __len__(self):
        return self.length

    def append(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('Full')

        node = Node(value)
        tailnode = self.tailnode

        if tailnode is None:  # 说明只有一个root节点
            self.root.next = node
        else:
            tailnode.next = node
        self.tailnode = node
        self.length += 1

    def appendleft(self, value):  # 每一个都插入到root节点的后面
        '''
        首节点在root节点之后
        将要插入的node节点插入到root的next
        将node.next指向之前的首节点
        '''
        headnode = self.root.next
        node = Node(value)
        self.root.next = node
        node.next = headnode
        self.length += 1

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node(self):
        currnode = self.root.next
        while currnode is not self.tailnode:
            yield currnode
            currnode = currnode.next
        yield currnode

    def remove(self, value):  # O(n)复杂度
        previrnode = self.root
        currnode = self.root.next

        for currnode in self.iter_node():     # 代替原 while currnode is not None
            if currnode.value == value:
                previrnode.next = currnode.next
                if currnode is self.tailnode:
                    self.tailnode = currnode
                del currnode
                self.length -= 1
                return 1  # 表示删除成功
            else:
                previrnode = currnode
            return -1


    def find(self, value):  # O(n)复杂度
        index = 0
        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return -1  # 用来标识

    def popleft(self):  # O(1)复杂度 ， 可用来实现两端队列
        if self.root.next is None:
            raise Exception('pop from empty Linkedlist')
        headnode = self.root.next
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value
        del headnode
        return value

    def clear(self):
        for node in self.iter_node():
            del node

        self.length = 0
        self.root.next = None
##############################
#       以下是queue实现
##############################
class FullError(Exception):
    pass

class EmptyError(Exception):
    pass

class Queue(object):
    def __init__(self, maxsize=None, ):
        self.maxsize = maxsize
        self._item_linked_list = Linkedlist()

    def __len__(self):
        return len(self._item_linked_list)

    def push(self, item):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise FullError('queue is full')
        return self._item_linked_list.append(item)

    def pop(self):
        if len(self) <= 0:
            raise EmptyError('queue is empty')
        return self._item_linked_list.popleft()

def test_queue():
    q = Queue()
    q.push(0)
    q.push(1)
    q.push(2)

    assert len(q) == 3

    assert q.pop() == 0
    assert q.pop() == 1
    assert q.pop() == 2
    
    import pytest
    with pytest.raises(EmptyError) as empinfo:
        q.pop()
    assert 'empty' in str(empinfo.value)

