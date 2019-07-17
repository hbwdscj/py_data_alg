# 实现单链表

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


def test_linkdelist():
    ll = Linkedlist()

    ll.append(0)
    ll.append(1)
    ll.append(2)

    assert list(ll) == [0, 1, 2,]
    assert len(ll) == 3
    assert ll.find(2) == 2

    ll.remove(0)
    assert len(ll) == 2
    assert ll.find(1) == 0

    ll.appendleft(0)
    assert len(ll) == 3
    assert ll.find(2) == 2

    popvalue = ll.popleft()
    assert popvalue == 0
    assert len(ll) == 2
    assert ll.find(2) == 1
    assert [node.value for node in ll.iter_node()] == [1, 2]
    

    ll.clear()
    assert len(ll) == 0


test_linkdelist()
# print(list(ll))        # right