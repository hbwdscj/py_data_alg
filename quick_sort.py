
def quick_sort(seq):
    if len(seq) <= 1:
        return seq
    else:
        pivot_index = 0  # TODO:后续采取选取pivot的优化措施
        pivot = seq[pivot_index]
        less_part = [i for i in seq[pivot_index + 1:] if i < pivot]
        great_part = [i for i in seq[pivot_index + 1:] if i > pivot]
        return quick_sort(less_part) + [pivot] + quick_sort(great_part)


def test_quick_sort():
    import random
    seq = list(range(10))
    random.shuffle(seq)
    print(quick_sort(seq))
    assert quick_sort(seq) == sorted(seq)