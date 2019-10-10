def bubble_sort(seq):
    n = len(seq)
    for i in range(n-1):
        print(seq)
        for j in range(n-1-i):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    print(seq)


def test_bubble_sort():
    import random
    a = list(range(10))
    random.shuffle(a)
    sorted_list = sorted(a)
    bubble_sort(a)
    assert a == sorted_list


def select_sort(seq):
    n = len(seq)
    for i in range(n-1):
        min_idx = i
        print(seq)
        for j in range(i+1, n):
            if seq[j] < seq[min_idx]:
                min_idx = j
        if min_idx != i:
            seq[i], seq[min_idx] = seq[min_idx], seq[i]
    print(seq)


def test_select_sort():
    import random
    a = list(range(10))
    random.shuffle(a)
    sorted_list = sorted(a)
    select_sort(a)
    assert a == sorted_list


def insert_sort(seq):
    n = len(seq)
    for i in range(1, n):
        value = seq[i]
        pos = i
        while pos > 0 and value < seq[pos-1]:
            seq[pos] = seq[pos-1]
            pos -= 1
        seq[pos] = value

