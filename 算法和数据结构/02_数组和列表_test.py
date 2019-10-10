"""
线性结构：1.内存空间连续 2.下标访问
python常用的array(很少用,不同于Numpy中的array)、
list方法  时间复杂度
下标访问 O(1)
append  O(1)
insert  O(n)
pop default the last element' O(1)
remove O(n)
"""


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


def test_array():
    size = 10
    a = Array(size)
    a[0] = 1
    assert a[0] == 1

    a.clear()

    assert a[0] is None


test_array()


