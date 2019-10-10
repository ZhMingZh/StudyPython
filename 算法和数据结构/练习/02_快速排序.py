def quick_sort(array):
    """快速排序， 参数是序列；传入其他类型会报错"""
    # V1.0
    # size = len(array)
    # if not array and size < 2:
    #     return array
    # pivot_idx = 0
    # pivot = array[pivot_idx]
    # less_part = [array[i] for i in range(size) if array[i] <= pivot and i != pivot_idx]
    # great_part = [array[i] for i in range(size) if array[i] > pivot and i != pivot_idx]
    # return quick_sort(less_part) + [pivot] + quick_sort(great_part)
    # V1.1
    if len(array) < 2:
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    great = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(great)


def test_quick_sort():
    import random
    array = list(range(20))
    # assert isinstance(array, list)
    random.shuffle(array)
    # assert 0
    assert quick_sort(array) == sorted(array)
    assert quick_sort([]) == []


def partition(array, beg, end):
    pivot_idx = beg
    pivot = array[pivot_idx]
    left = pivot_idx + 1
    right = end - 1

    while True:
        # 从左边找到比pivot大的值，否则就一直left+1
        while left <= right and array[left] < pivot:
            left += 1
        # 从右边找到比pivot小的值，否则end一直-1
        while right >= left and array[right] >= pivot:
            right -= 1

        if left > right:
            break
        array[left], array[right] = array[right], array[left]   # 交换left和right对应的值
    array[pivot_idx], array[right] = array[right], array[pivot_idx]  # 将主元与right(其实是right-1)位置的值交换
    return right


def quick_sort_inplace(array, beg, end):
    if beg < end:
        pivot = partition(array, beg, end)
        quick_sort_inplace(array, beg, pivot)
        quick_sort_inplace(array, pivot + 1, end)


def test_quick_sort_inplace():
    import random
    array = list(range(5))
    random.shuffle(array)
    quick_sort_inplace(array, 0, len(array))
    assert array == [0, 1, 2, 3, 4]


def nth_element(array, beg, end, nth):
    """查找一个数组的第n小的元素 ?"""
    if beg < end:
        pivot = partition(array, beg, end)
        if pivot == nth - 1:
            return array[pivot]
        elif pivot > nth - 1:
            return nth_element(array, beg, pivot, nth)
        else:
            return nth_element(array, pivot + 1, end, nth)


def test_nth_element():
    l1 = [3, 5, 4, 2, 1]
    assert nth_element(l1, 0, len(l1), 1) == 1
    assert nth_element(l1, 0, len(l1), 4) == 4

