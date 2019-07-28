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
def binary_search_recursion(sorted_value, val):
    beg = 0
    end = len(sorted_value) - 1
    while beg <= end:
        mid = int((beg+end)/2)
        if sorted_value[mid] == val:
            return mid
        elif sorted_value[mid] < val:
            new_sorted_value = sorted_value[mid:end]
            return binary_search_recursion(new_sorted_value, val)
        else:
            new_sorted_value = sorted_value[beg:mid]
            return binary_search_recursion(new_sorted_value, val)


a = list(range(4))

b1 = binary_search_recursion(a, 0)
b2 = binary_search_recursion(a, 1)
b3 = binary_search_recursion(a, 2)
b4 = binary_search_recursion(a, 3)

print("%s, %s, %s, %s," %(b1, b2, b3, b4))
