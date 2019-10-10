def merge_sort(seq):
    """归并排序"""
    if len(seq) <= 1:
        return seq
    else:
        mid = int(len(seq) / 2)
        left_half = merge_sort(seq[:mid])
        right_half = merge_sort(seq[mid:])
        # 合并两个有序序列
        new_seq = merge_sorted_list(left_half, right_half)
        return new_seq


def merge_sorted_list(sorted_a, sorted_b):
    """合并两个有序序列，返回一个新的有序序列"""
    length_a, length_b = len(sorted_a), len(sorted_b)
    a = b = 0
    new_sorted_seq = list()
    while a < length_a and b < length_b:
        if sorted_a[a] < sorted_b[b]:
            new_sorted_seq.append(sorted_a[a])
            a += 1
        else:
            new_sorted_seq.append(sorted_b[b])
            b += 1
    # 剩余的元素加入到有序数组
    if a < length_a:
        new_sorted_seq.extend(sorted_a[a:])
    else:
        new_sorted_seq.extend(sorted_b[b:])

    return new_sorted_seq


def test_merge_sort():
    import random
    a = list(range(4))
    random.shuffle(a)
    sorted_list = merge_sort(a)
    assert sorted_list == sorted(a)


def quick_sort(array):
    size = len(array)
    if not array and size < 2:
        return array
    pivot_idx = 0
    pivot = array[pivot_idx]
    less_part = [array[i] for i in range(size) if array[i] <= pivot and pivot_idx != i]
    great_part = [array[i] for i in range(size) if array[i] > pivot and pivot_idx != i]
    return quick_sort(less_part) + [pivot] + quick_sort(great_part)


def test_quick_sort():

    import random
    seq = list(range(10))
    random.shuffle(seq)
    sorted_list = quick_sort(seq)
    assert sorted_list == sorted(seq)


def partition(array, beg, end):
    """对给定数组执行partition操作，返回pivot位置"""
    pivot_index = beg
    pivot = array[pivot_index]
    left = pivot_index + 1
    right = end - 1

    while True:
        # 从左边找到比 pivot 大的
        while left <= right and array[left] < pivot:
            left += 1
        # 从右边找到比 pivot 小的
        while right >= left and array[right] >= pivot:
            right -= 1

        if left > right:
            break

        array[left], array[right] = array[right], array[left]

    array[pivot_index], array[right] = array[right], array[pivot_index]
    return right


def test_partition():
    l = [1, 3, 2, 4]
    assert partition(l, 0, len(l)) == 0
    l = [2, 3, 5, 1]
    assert partition(l, 0, len(l)) == 1
    l = [4, 3, 2, 1]
    assert partition(l, 0, len(l)) == 3


def quick_sort_inplace(array, beg, end):
    if beg < end:
        pivot = partition(array, beg, end)
        quick_sort_inplace(array, beg, pivot)
        quick_sort_inplace(array, pivot+1, end)


def test_quicksort_inplace():
    import random
    seq = list(range(10))
    sorted_seq = sorted(seq)
    random.shuffle(seq)
    quick_sort_inplace(seq, 0, len(seq))
    assert seq == sorted_seq


def nth_element(array, beg, end, nth):
    """查找一个数组第n大的元素"""
    if beg < end:
        pivot_idx = partition(array, beg, end)
        if pivot_idx == nth - 1:
            return array[pivot_idx]
        elif pivot_idx > nth - 1:
            return nth_element(array, beg, pivot_idx, nth)
        else:
            return nth_element(array, pivot_idx + 1, end, nth)


def test_nth_element():
    # l1 = [1, 3, 5, 0]
    # assert nth_element(l1, 0, len(l1), 1) == 5
    l1 = [3, 5, 4, 2, 1]
    assert nth_element(l1, 0, len(l1), 3) == 3
    assert nth_element(l1, 0, len(l1), 2) == 2

    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in l:
        assert nth_element(l, 0, len(l), i) == i
    for i in reversed(l):
        assert nth_element(l, 0, len(l), i) == i

    array = [3, 2, 1, 5, 6, 4]
    assert nth_element(array, 0, len(array), 2) == 2

    array = [2, 1]
    assert nth_element(array, 0, len(array), 1) == 1
    assert nth_element(array, 0, len(array), 2) == 2

    array = [3, 3, 3, 3, 3, 3, 3, 3, 3]
    assert nth_element(array, 0, len(array), 1) == 3

    l2 = [1, 3, 5, 6]
    assert nth_element(l2, 0, len(l2), 4) == 1