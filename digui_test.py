from collections import deque


def fact(n):
    if n==0 :
        return 1
    else:
        return n*fact(n-1)

def print_num_0_10(n):
    if n > 0:
        print(n)
        print_num_0_10(n-1)

class Stack(object):
    """
    用栈来模拟递归内部操作
    """
    def __init__(self):
        self._deque = deque()   
        
    def push(self, value):
        return self._deque.append(value)
    
    def pop(self):
        return self._deque.pop()

    def is_empty(self,):
        return len(self._deque) == 0

def print_num_use_stack(n):
    s = Stack()
    while n > 0:
        s.push(n)
        n -= 1

    while not s.is_empty():
        print(s.pop())

