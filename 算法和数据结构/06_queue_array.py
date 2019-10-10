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


class FullError(Exception):
    pass


class ArrayQueue(object):
    """当进行push操作时head +1，

    """
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.array = Array()
        self.head = 0
        self.tail = 0

    def __len__(self):
        return self.head - self.tail

    def push(self, value):
        if len(self) >= self.maxsize:
            raise FullError('full')
        self.array[self.head % self.maxsize] = value
        self.head += 1

    def pop(self):
        value = self.array[self.tail % self.maxsize]
        self.tail += 1
        return value


def test_array_queue():
    import pytest
    size = 5
    q = ArrayQueue(size)
    for i in range(size):
        q.push(i)

    assert len(q) == 5
    with pytest.raises(FullError) as excinfo:
        q.push(size)

    assert 'full' in str(excinfo.value)

    assert q.pop() == 0
    assert q.pop() == 1
    assert q.pop() == 2
    assert q.pop() == 3
    assert q.pop() == 4

    assert len(q) == 0