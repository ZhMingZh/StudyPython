import random


def bubble_sort(seq):
    """冒泡排序"""
    n = len(seq)
    for i in range(n-1):
        for j in range(n-1-i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]


def test_bubble_sort():
    seq = list(range(10))
    random.shuffle(seq)
    sorted_list = sorted(seq)
    bubble_sort(seq)
    assert seq == sorted_list


def select_sort(seq):
    """选择排序"""
    n = len(seq)
    for i in range(n-1):
        min_indx = i
        for j in range(i+1, n):   # i+1
            if seq[j] < seq[min_indx]:
                min_indx = j
        if min_indx != i:
            seq[i], seq[min_indx] = seq[min_indx], seq[i]


def test_select_sort():
    seq = list(range(10))
    random.shuffle(seq)
    sorted_list = sorted(seq)
    select_sort(seq)
    assert seq == sorted_list


def insert_sort(seq):
    """插入排序"""
    n = len(seq)
    for i in range(1, n):
        value = seq[i]
        pos = i
        while pos > 0 and value < seq[pos-1]:
            seq[pos] = seq[pos-1]
            pos -= 1
        seq[pos] = value


def test_insert_sort():
    seq = list(range(10))
    random.shuffle(seq)
    sorted_list = sorted(seq)
    insert_sort(seq)
    assert seq == sorted_list
