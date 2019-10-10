def merge_sort(seq):
    """归并排序 把一个数组的元素一分为二，一直递归，直到每一个数组都有一个元素组成，再逐一将两个有序的数组合并"""
    if len(seq) <= 1:  # 递归出口
        return seq
    else:
        mid = int(len(seq) / 2)
        left_part = merge_sort(seq[:mid])
        right_part = merge_sort(seq[mid:])

        # 合并两个有序数组
        new_seq = merge_sorted_list(left_part, right_part)
        return new_seq


def merge_sorted_list(sorted_a, sorted_b):
    """"合并两个有序的序列"""
    length_a, length_b = len(sorted_a), len(sorted_b)
    a = b = 0
    new_sorted_seq = list()
    while a < length_a and b < length_b:   # 当两个列表都有可以比较的元素才进入循环
        if sorted_a[a] < sorted_b[b]:
            new_sorted_seq.append(sorted_a[a])
            a += 1
        else:
            new_sorted_seq.append(sorted_b[b])
            b += 1
    # a或b中剩余的元素,合并两个列表用extend
    if a < length_a:
        new_sorted_seq.extend(sorted_a[a:])
    else:
        new_sorted_seq.extend(sorted_b[b:])

    return new_sorted_seq


def test_merge_sort():
    import random
    seq = list(range(20))
    random.shuffle(seq)
    assert merge_sort(seq) == sorted(seq)