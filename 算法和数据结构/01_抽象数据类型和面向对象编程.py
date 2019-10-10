"""
ADT: abstract data type
注意：1.选用数据结构 DataStructure 2.选用的数据结构是否满足操作 3.效率
"""


class Bag(object):
    """Bag ADT"""
    def __init__(self, maxsize=10):
        self.maxsize = maxsize
        self._items = list()

    def add(self, item):
        if len(self._items) > self.maxsize:
            raise Exception("Bag is Full")
        self._items.append(item)

    def remove(self, item):
        self._items.remove(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        for item in self._items:
            yield item


def test_bag():
    bag = Bag()
    bag.add(1)
    bag.add(2)
    bag.add(3)

    assert len(bag) == 3

    bag.remove(3)

    assert len(bag) == 2

    for item in bag:
        print(item)


test_bag()