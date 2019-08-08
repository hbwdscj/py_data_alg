# 1.反转链表
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
        return self._item_deque.pop()

    def push(self, value):
        return self._item_deque.append(value)

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

        """
        以下为用栈实现翻转列表
        """

def rvs_ll(ll):
    stc = Stack()
    new_ll = Linkedlist()
    length_stc = 0
    length_ll = len(ll)
    while length_ll > 0:
        stc.push(ll.popleft())
        length_stc += 1
        length_ll -= 1
    
    while length_stc > 0 and length_ll <= 0:
        new_ll.append(stc.pop())
        length_stc -= 1
    return new_ll


# 三个指针翻转链表
def rvs_ll_2(ll):
    p = ll.root.next
    ll.tailnode = p
    r = None

    while p:
        q = p.next
        p.next = r
        if q is None:
            ll.root.next = p
        r = p
        p = q
    return ll

    
def main():
    ll = Linkedlist()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    print("ll is :"+ str(list(ll)))
    new_ll = rvs_ll_2(ll)
    print("new_ll is : " + str(list(new_ll)))


if __name__ == "__main__":
    main()
            
