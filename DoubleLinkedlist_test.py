class Node(object):
    __slots__ = ('value', 'prev', 'next')

    def __init__(self, value=None, prev=None, next=None):
        self.value, self.next, self.prev = value, next, prev


class CircualDoubleLinkedlist(object):
    def __init__(self, maxsize=None,):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.length = 0
        self.root = node

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):
        '''
        新增节点理论步骤:
        1.构造一个新节点
        2.原tail节点next指向新节点，新节点prev指向原tail节点
        3.新节点的next指向root节点，root节点的prev指向新节点
        4.length加1
        '''
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('Full')
        node = Node(value=value)
        tailnode = self.tailnode() or self.root   # 由此想到定义两个新方法，获取head和tail节点
        
        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1
    
    def appendleft(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('Full')
        node = Node(value=value)

        if self.root.next is self.root:    # 若链表为空
            node.next = self.root
            node.prev = self.root
            self.root.next = node
            self.root.prev = node
        else:
            node.prev = self.root
            headnode = self.headnode()
            node.next = headnode
            headnode.prev = node
            self.root.next = node
        self.length += 1

    def popleft(self):
        if len(self) <= 0:
            raise Exception("pop from an empty list")
        else:
            headnode = self.root.next
            self.root.next = headnode.next
            headnode.next.prev = self.root                       
            value = headnode.value
            del headnode   
            self.length -= 1
            return value

    def pop(self):
        if len(self) <= 0:
            raise Exception("pop from an empty list")
        else:
            tailnode = self.root.prev
            self.root.prev = tailnode.prev
            tailnode.prev.next = self.root
            value = tailnode.value
            del tailnode
            self.length -= 1
            return value

    def remove(self, node):      # O(1)  node not value 
        if node is self.root:
            return 
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node
    
    def iter_node(self):
        if self.root.next is self.root:
            return 
        currnode = self.root.next
        while currnode.next is not self.root:
            yield currnode
            currnode = currnode.next
        yield currnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        if self.root.prev is self.root:
            return 
        currnode = self.root.prev
        while currnode.prev is not self.root:
            yield currnode
            currnode = currnode.prev   
        yield currnode

def test_double_linked_list():
    dll = CircualDoubleLinkedlist()
    assert len(dll) == 0

    dll.append(0)
    dll.append(1)
    dll.append(2)

    assert[node.value for node in dll.iter_node()] == [0, 1, 2]
    assert[node.value for node in dll.iter_node_reverse()] == [2, 1, 0]  

    headnode = dll.headnode()
    assert headnode.value == 0 
    dll.remove(headnode)
    assert len(dll) == 2
    assert [node.value for node in dll.iter_node()] == [1, 2]   

    dll.appendleft(0)
    assert [node.value for node in dll.iter_node()] == [0, 1, 2]        
        
    popa = dll.pop()
    assert popa == 2
    assert len(dll) == 2

    popb = dll.popleft()
    assert popb == 0
    assert len(dll) == 1

    assert [node.value for node in dll.iter_node()] == [1]































