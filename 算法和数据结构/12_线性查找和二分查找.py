number_list = [0, 2, 1, 4, 5, 10, 9]


def linear_search(value, iterable):
    for index, val in enumerate(iterable):
        if val == value:
            return index
    return -1


assert linear_search(10, number_list) == 5


def linear_search_v2(predicate, iterable):
    for index, val in enumerate(iterable):
        if predicate(val):
            return index
    return -1


assert linear_search_v2(lambda x: x == 9, number_list) == 6


def linear_search_recursive(array, value):
    if len(array) == 0:
        return -1
    index = len(array) - 1
    if array[index] == value:
        return index
    return linear_search_recursive(array[0:index], value)


assert linear_search_recursive(number_list, 0) == 0
assert linear_search_recursive(number_list, 9) == 6
assert linear_search_recursive(number_list, 20) == -1


# ========================================
# 下面是二分查找， 针对的是有序的数组
# ========================================
sorted_list = sorted(number_list)


def binary_search(sorted_array, val):
    if not sorted_array:
        return -1
    start = 0
    end = len(sorted_array) - 1
    while start <= end:
        mid = int((start + end) / 2)
        if sorted_array[mid] == val:
            return mid
        elif sorted_array[mid] > val:
            end = mid - 1
        else:
            start = mid + 1
    return -1


assert binary_search(sorted_list, 0) == 0
assert binary_search(sorted_list, 12) == -1


def binary_search_recusive(sorted_array, start, end, val):
    if start >= end:
        return -1
    mid = int((start + end) / 2)
    if sorted_array[mid] == val:
        return mid
    elif sorted_array[mid] > val:
        return binary_search_recusive(sorted_array, start, mid, val)
    else:
        return binary_search_recusive(sorted_array, mid+1, end, val)


def test_binary_search_recusive():
    a = list(range(10))
    assert binary_search_recusive(a, 0, len(a), 0) == 0
    assert binary_search_recusive(a, 0, len(a), 9) == 9
    assert binary_search_recusive(a, 0, len(a), 10) == -1
    assert binary_search_recusive(a, 0, len(a), 6) == 6


