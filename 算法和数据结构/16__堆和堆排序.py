class Array(object):
    """用list实现 Array ADT"""
    def __init__(self, size=32):
        self.size = size
        self._items = [None] * size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, key, value):
        self._items[key] = value

    def __len__(self):
        return self.size

    def __iter__(self):
        for item in self._items:
            yield item

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value


class MaxHeap(object):
    """最大堆"""
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len__(self):
        return self._count

    def add(self, value):
        if self._count >= self.maxsize:
            raise Exception('full')
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count - 1)

    def _siftup(self, idx):
        if idx > 0:
            parent = int((idx-1) / 2)
            if self._elements[idx] > self._elements[parent]:
                self._elements[idx], self._elements[parent] = self._elements[parent], self._elements[idx]
                self._siftup(parent)

    def extract(self):
        if self._count <= 0:
            raise Exception('empty')
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        self._siftdown(0)
        return value

    def _siftdown(self, idx):
        left = idx * 2 + 1
        right = idx * 2 + 2
        largest = idx
        if (left < self._count and
                self._elements[left] > self._elements[right] and
                self._elements[left] > self._elements[largest]):
            largest = left
        elif right < self._count and self._elements[right] > self._elements[largest]:
            largest = right
        if largest != idx:
            self._elements[idx], self._elements[largest] = self._elements[largest], self._elements[idx]
            self._siftdown(largest)


def test_maxheap():
    n = 5
    h = MaxHeap(n)
    for i in range(n):
        h.add(i)

    assert len(h) == 5

    # print(list(reversed(range(n))))
    for i in reversed(range(n)):
        assert h.extract() == i


def heap_sort(array):
    """堆排序"""
    length = len(array)
    maxheap = MaxHeap(length)
    for i in array:
        maxheap.add(i)
    seq = []
    for i in range(length):
        seq.append(maxheap.extract())
    return seq


def test_heap_sort():
    import random
    l = list(range(10))
    random.shuffle(l)
    sorted_list = heap_sort(l)
    assert sorted_list == sorted(l, reverse=True)


class PriorityQueue(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self._maxheap = MaxHeap(maxsize)

    def push(self, priority, value):
        # 注意这里把这个 tuple push 进去，python 比较 tuple 从第一个开始比较
        # 这样就很巧妙地实现了按照优先级排序
        entry = (priority, value)
        self._maxheap.add(entry)

    def pop(self, with_priority=False):
        entry = self._maxheap.extract()
        if with_priority:
            return entry
        else:
            return entry[1]

    def is_empty(self):
        return len(self._maxheap) == 0


def test_priority_queue():
    size = 5
    pq = PriorityQueue(size)
    pq.push(5, 'purple')    # priority, value
    pq.push(0, 'white')
    pq.push(3, 'orange')
    pq.push(1, 'black')

    res = []
    while not pq.is_empty():
        res.append(pq.pop())

    assert res == ['purple', 'orange', 'black', 'white']











