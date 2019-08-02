"""
def binary_search(sorted_list, val):
    if not sorted_list:
        return -1

    beg = 0
    end = len(sorted_list) - 1
    while beg <= end:
        mid = int((beg+end)/2)
        if sorted_list[mid] ==  val:
            return mid
        elif sorted_list[mid] < val:
            beg = mid + 1
        else:
            beg = mid - 1
    return -1
"""
import sys
sys.setrecursionlimit(1000)
def binary_search_recursion(sorted_value, beg, end, val):  
    if beg >= end:
        return -1
    mid = int((beg+end)/2)
    if sorted_value[mid] == val:
        return mid
    elif sorted_value[mid] < val:
        return binary_search_recursion(sorted_value, mid+1, end, val)
    else:
        return binary_search_recursion(sorted_value, beg, mid, val)
"""

#错误记录：第一版实现出现错误是因为将sorted_value切片传入新的递归函数，导致序列的下标志
#出现改变，因此返回的mid值不是最开始sorted_value的下标，循环部分代码如下:
if sorted_value[mid] == val:
    return mid
elif sorted_value[mid] < val:
    return binary_search_recursion(sorted_value[mid:end], val) 此处切片就会产生一个新的list，导致下标改变

"""

a = list(range(4))
b1 = binary_search_recursion(a, 0, len(a), 0)
b2 = binary_search_recursion(a, 0, len(a), 1)
b3 = binary_search_recursion(a, 0, len(a), 2)
b4 = binary_search_recursion(a, 0, len(a), 3)
b5 = binary_search_recursion(a, 0, len(a), 10)
print("%s, %s, %s, %s, %s" %(b1, b2, b3, b4, b5))
