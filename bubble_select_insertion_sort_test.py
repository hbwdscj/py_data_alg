import random   

def bubble_sort(seq):
    n = len(seq)
    for i in range(n-1): # 定义为进行n-1轮迭代，因为最后一轮已经有序   
        print(seq) 
        for j in range(n-1-i): # 第i轮迭代的时候，已经有i+1个元素排好序了，比如i=2时，已经有3个元素排好序了，因此j范围为n-(i+1)
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    print(seq)

def test_bubble_sort():
    seq = list(range(10))
    random.shuffle(seq)
    bubble_sort(seq)
    assert seq == sorted(seq)

def select_sort(seq):
    n = len(seq)
    for i in range(n-1):
        min_index = i 
        """
        基本思路为：
        假设i是最小元素，然后遍历i后的所有元素，如果发现比i小的元素，将其index赋给min_index
        min_index即为每轮遍历中的最小元素,
        最后if判断，如果min_index不是i（即首位元素）的话，将其赋值给i，即放置在此轮遍历的首位
        n-1轮遍历过后元素排序完成
        """
        print(seq)
        for j in range(i+1, n):
            if seq[j] < seq[min_index]:
                min_index = j
        if min_index != i:
            seq[min_index], seq[i] = seq[i], seq[min_index]
    print(seq)

def test_bubble_sort():
    seq = list(range(10))
    random.shuffle(seq)
    select_sort(seq)
    assert seq == sorted(seq)

def insertion_sort(seq):
    n = len(seq)
    for i in range(1, n): 
        print(seq)
        value = seq[i]
        pos = i
        while pos > 0 and value < seq[pos-1]:  # seq[pos-1] > value说明后面的比前面大
            seq[pos] = seq[pos-1]
            pos -= 1
        seq[pos] = value
        print(seq)


seq = list(range(10))
random.shuffle(seq)
insertion_sort(seq)