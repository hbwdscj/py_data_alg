

def quick_sort_1(seq):
    if len(seq) <= 1:
        return seq
    else:
        pivot_index = 0  # TODO:后续采取选取pivot的优化措施
        pivot = seq[pivot_index]

        # 此处新开了存储空间，不是inplace
        # 进行了两次遍历来实现partition操作哦

        less_part = [i for i in seq[pivot_index + 1:] if i < pivot]
        great_part = [i for i in seq[pivot_index + 1:] if i > pivot]
        return quick_sort_1(less_part) + [pivot] + quick_sort_1(great_part)


def partition_inplace(seq, beg, end):
    pivot_index = beg 
    pivot = seq[pivot_index]
    left = pivot_index + 1
    right = end - 1  

    while True:
        while left <= right and seq[left] < pivot:
            left += 1                  
        while right >= left and seq[right] > pivot:
            right -= 1
        if left > right:
            break
        else:
            seq[left], seq[right] = seq[right], seq[left]
    seq[pivot_index], seq[right] = seq[right], seq[pivot_index]
    return right # 返回主元的位置


def quick_sort_inplace(seq, beg, end): # 左闭右开区间
    if beg < end:
        pivot = partition_inplace(seq, beg, end)
        quick_sort_inplace(seq, beg, pivot)
        quick_sort_inplace(seq, pivot+1, end)


def test_partition_inplace():
    l = [3, 4, 1, 2,]
    assert partition_inplace(l, 0, len(l)) == 2
    


def test_quick_sort():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    print(quick_sort_1(seq))
    assert quick_sort_1(seq) == sorted(seq)

def test_quick_sort_inplace():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    quick_sort_inplace(seq, 0, len(seq))
    print(seq)
    assert seq == sorted(seq)

    
test_partition_inplace()