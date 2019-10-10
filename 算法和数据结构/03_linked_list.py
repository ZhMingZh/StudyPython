"""单向链表"""


class Node(object):
    """节点"""
    def __init__(self, value=None, next=None):  # 根结点默认值为None
        self.value = value
        self.next = next

    def __str__(self):
        return '<Node: value: {}, next: {}>'.format(self.value, self.next)

    __repr__ = __str__


class LinkedList(object):
    """单链表"""
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value)  # 构造新节点
        tailnode = self.tailnode
        if tailnode is None:  # 还没有append过，length=0， 直接追加到root后面
            self.root.next = node
        else:  # 否则追加到最后一个节点的后边，并且更新最后一个节点是append的节点
            tailnode.next = node
        self.tailnode = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value)
        if self.tailnode is None:
            self.tailnode = node

        headnode = self.root.next
        self.root.next = node
        node.next = headnode
        self.length += 1

    def iter_node(self):
        """遍历从head节点到tail节点"""
        curnode = self.root.next
        while curnode is not self.tailnode:  # 从第一个节点开始遍历
            yield curnode
            curnode = curnode.next  # 移动到下一个节点
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def remove(self, value):
        """删除包含值的一个节点，将其一个前节点的next指向被查询的节点的下一个即可"""
        prevnode = self.root
        for curnode in self.iter_node():
            if curnode.value == value:
                prevnode.next = curnode.next
                if curnode is self.tailnode:
                    self.tailnode = prevnode
                del curnode
                self.length -= 1
                return 1  # 代表成功
            else:
                prevnode = curnode
        return -1  # 没找到

    def find(self, value):
        """查询一个节点，返回序号，从0开始"""
        index = 0
        for curnode in self.iter_node():
            if curnode.value == value:
                return index
            index += 1
        return -1  # 没找到

    def popleft(self):
        """删除第一个链表节点"""
        if self.root.next is None:
            raise Exception('pop from empty LinkedList')
        headnode = self.root.next
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value

        if self.tailnode is headnode:
            self.tailnode = None
        del headnode
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.tailnode = None
        self.length = 0

    def reverse(self):
        """反转链表
            prev 前一个节点 cur 当前节点 next 下一个节点
            prevnode = curnode
            curnode = nextcode
            不断循环以上两个操作（当前节点指向向节点，下一个节点指向当前节点），直到curnode=None,
        """

        curnode = self.root.next  # 头节点
        self.tailnode = curnode
        prevnode = None

        while curnode:
            nextcode = curnode.next
            curnode.next = prevnode

            if nextcode is None:
                self.root.next = curnode

            prevnode = curnode
            curnode = nextcode


def test_linked_list():
    ll = LinkedList()

    ll.append(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)

    assert len(ll) == 4
    assert ll.find(2) == 2
    assert ll.find(-1) == -1

    assert ll.remove(0) == 1
    assert ll.remove(10) == -1
    assert ll.remove(2) == 1
    assert len(ll) == 2
    assert list(ll) == [1, 3]
    assert ll.find(0) == -1

    ll.appendleft(0)
    assert list(ll) == [0, 1, 3]
    assert len(ll) == 3

    headvalue = ll.popleft()
    assert headvalue == 0
    assert len(ll) == 2
    assert list(ll) == [1, 3]

    assert ll.popleft() == 1
    assert list(ll) == [3]
    ll.popleft()
    assert len(ll) == 0
    assert ll.tailnode is None

    ll.clear()
    assert len(ll) == 0
    assert list(ll) == []


def test_linked_list_remove():
    ll = LinkedList()
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.remove(7)
    print(list(ll))


def test_linked_list_reverse():
    ll = LinkedList()
    n = 10
    for i in range(n):
        ll.append(i)
    ll.reverse()
    assert list(ll) == list(reversed(range(n)))


def test_linked_list_append():
    ll = LinkedList()
    ll.appendleft(1)
    ll.append(2)
    assert list(ll) == [1, 2]


if __name__ == '__main__':
    test_linked_list()
    test_linked_list_append()
    test_linked_list_reverse()