class Array(object):
    """用list实现 Array ADT"""

    def __init__(self, size=32, init=None):
        self.size = size
        self._items = [init] * size

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


class Slot(object):
    """
    定义一个Hash表 数组的槽，3种状态
    1 HASHMAP.UNUSED 此槽没有被使用和冲突过，查找时只要找到 UNUSED 就不用再继续探查了
    2 使用过但是 remove 了，此时是 HashMap.EMPTY，该探查点后边的元素扔可能是有key
    3 槽正在使用 Slot 节点
    """

    def __init__(self, key, value):
        self.key, self.value = key, value


class HashTable(object):
    """哈希表"""
    UNUSED = None
    EMPTY = Slot(None, None)

    def __init__(self):
        self._table = Array(8, init=HashTable.UNUSED)
        self.length = 0

    def __len__(self):
        return self.length

    @property
    def _load_factor(self):
        # load_factor 超过 0.8 重新分配
        return self.length / float(len(self._table))

    def _hash(self, key):
        return abs(hash(key)) % len(self._table)

    def _find_key(self, key):
        """此函数是寻找存在self._table中slot的key(还不是很理解）"""
        index = self._hash(key)
        _len = len(self._table)
        # （UNUSED为此槽没有被使用和冲突过），也就是当前index对应的槽是使用用或冲突过的才进入循环
        while self._table[index] is not HashTable.UNUSED:
            if self._table[index] is HashTable.EMPTY:  # 为啥槽是清除过的空的，还需要在计算一次key,得到新的index
                index = (index * 5 + 1) % _len  # CPython的探查方法
            elif self._table[index].key == key:
                return index
            else:
                index = (index * 5 + 1) % _len
        return None

    def _slot_can_insert(self, index):
        return self._table[index] is HashTable.UNUSED or self._table[index] is HashTable.EMPTY

    def _find_slot_for_insert(self, key):
        index = self._hash(key)
        _len = len(self._table)
        while not self._slot_can_insert(index):
            index = (index * 5 + 1) % _len
        return index

    def __contains__(self, key):
        index = self._find_key(key)
        return index is not None

    def add(self, key, value):
        if key in self:  # update
            index = self._find_key(key)
            self._table[index].value = value
            return False
        else:
            index = self._find_slot_for_insert(key)
            self._table[index] = Slot(key, value)   # add
            self.length += 1
            if self._load_factor > 0.8:
                self._rehash()
            return True

    def __iter__(self):
        for slot in self._table:
            if slot not in (HashTable.UNUSED, HashTable.EMPTY):  # 迭代使用中的槽
                yield slot.key

    def _rehash(self):
        old_table = self._table
        newsize = len(self._table) * 2
        self._table = Array(newsize, init=HashTable.UNUSED)
        self.length = 0

        for slot in old_table:
            # __iter__ 已经将未使用的槽剔除，因此无需在判断
            if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:
                index = self._find_slot_for_insert(slot.key)
                self._table[index] = slot
                self.length += 1

    def get(self, key, default=None):
        index = self._find_key(key)
        if index is None:
            return default
        else:
            return self._table[index].value

    def remove(self, key):
        index = self._find_key(key)
        if index is None:
            raise KeyError()
        else:
            value = self._table[index].value
            self.length -= 1
            self._table[index] = HashTable.EMPTY
            return value


class SetADT(HashTable):

    def add(self, key):
        return super(SetADT, self).add(key, True)

    def __and__(self, other_set):
        """A&B"""
        new_set = SetADT()
        for element_a in self:
            if element_a in other_set:
                new_set.add(element_a)
        return new_set

    def __sub__(self, other_set):
        """A-B 返回在A中的元素不在B中的"""
        new_set = SetADT()
        for element_a in self:
            if element_a not in other_set:
                new_set.add(element_a)
        return new_set

    def __or__(self, other_set):
        """A|B"""
        new_set = SetADT()
        for element_a in self:
            new_set.add(element_a)
        for element_b in other_set:
            new_set.add(element_b)
        return new_set

    def __xor__(self, other_set):
        """A|B - A&B 对称差集"""
        union = self.__or__(other_set)
        intersection = self.__and__(other_set)
        new_set = union.__sub__(intersection)
        return new_set


def test_set():
    sa = SetADT()
    sa.add(1)
    sa.add(2)
    sa.add(3)

    sb = SetADT()
    sb.add(3)
    sb.add(4)
    sb.add(5)

    assert list(sa & sb) == [3]
    assert sorted(list(sa | sb)) == [1, 2, 3, 4, 5]
    assert sorted(list((sa - sb))) == [1, 2]
    assert sorted(list(sa ^ sb)) == [1, 2, 4, 5]
