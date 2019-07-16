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
"""

# 此处的pop() 和 popleft()是针对实现一，实线二方法更为准确

    def popleft(self):
        '''
        删除头节点
        '''
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
        '''
        删除尾节点
        '''
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
"""
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

#####################################
# 以下为Deque实现 1
#####################################
'''
class FullError(Exception):
    pass

class EmptyError(Exception):
    pass    

class Deque(object):
    def __init__(self, maxsize=None, ):
        self.maxsize = maxsize
        self._item_cd_linked_list = CircualDoubleLinkedlist()
    
    def __len__(self):
        return len(self._item_cd_linked_list)

    def push(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise FullError('Dequeue is full')
        else:
            return self._item_cd_linked_list.append(value)
    
    def pushleft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise FullError('Dequeue is full')
        else:
            return self._item_cd_linked_list.appendleft(value)
    
    def pop(self):
        if len(self) <= 0:
            raise EmptyError('Dequeue is empty')
        else:
            return self._item_cd_linked_list.pop()
    
    def popleft(self):
        if len(self) <= 0:
            raise EmptyError('Dequeue is empty')
        else:
            return self._item_cd_linked_list.popleft()
'''

#################################
# 以下为Deque实现2
#################################
class Deque(CircualDoubleLinkedlist):
    
    def pop(self):
        if len(self) <= 0:
            raise Exception("empty")
        tailnode = self.tailnode()
        value = tailnode.value
        self.remove(tailnode)
        return value
    
    def popleft(self):
        if len(self) <= 0:
            raise Exception("empty")
        headnode = self.headnode()
        value = headnode.value
        self.remove(headnode)
        return value


class Stack(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._item_deque = Deque()
        
    def __len__(self):
        return len(self._item_deque)
    
    def pop(self):
        return _item_deque.pop()

    def push(self, value):
        return _item_deque.push(value)