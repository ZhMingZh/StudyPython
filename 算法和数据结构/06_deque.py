class Node(object):
    __slots__ = ('value', 'prev', 'next')

    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class CircularDoubleLinkedList:
    """
    循环双端链表 ADT
    多了个循环就是root的prev指向tail节点，串起来
    """
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.prev, node.next = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('CircularDoubleLinkedList is full')
        tailnode = self.tailnode() or self.root
        node = Node(value=value)

        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('CircularDoubleLinkedList is full')
        node = Node(value)
        if self.root.next is self.root:  # empty
            node.prev = self.root
            node.next = self.root
            self.root.prev = node
            self.root.next = node
        else:
            headnode = self.headnode()
            node.prev = self.root
            node.next = headnode
            headnode.prev = node
            self.root.next = node
        self.length += 1

    def remove(self, node):
        """O(1)传入node而不是value，我们就能实现O(1)"""
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node

    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode = self.root.next
        while curnode.next is not self.root: # is the last node ?
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        """反序遍历"""
        if self.root.prev is self.root:
            return
        curnode = self.root.prev
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode

    def insert(self, value, new_value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('full')
        for curnode in self.iter_node():
            if curnode.value == value:
                node = Node(new_value)
                curnode.prev.next = node
                curnode.prev = node
                node.prev = curnode
                node.next = curnode
                return 1  # success
            else:
                curnode = curnode.next
        return -1


# ============================================
# 下边是队列 deque 的实现
# ============================================
class EmptyError(Exception):
    pass


class Deque(CircularDoubleLinkedList):
    """继承循环双端链表
        实现append、appendleft、pop、popleft
    """
    def pop(self):
        if len(self) == 0:
            raise EmptyError('empty')
        tailnode = self.tailnode()
        value = tailnode.value
        self.remove(tailnode)
        return value

    def popleft(self):
        if len(self) == 0:
            raise EmptyError('empty')
        headnode = self.headnode()
        value = headnode.value
        self.remove(headnode)
        return value


def test_deque():

    q = Deque()
    size = 5
    for i in range(size):
        q.append(i)

    assert len(q) == 5

    q.appendleft(5)
    assert list(q) == [5, 0, 1, 2, 3, 4]

    q.pop()
    assert list(q) == [5, 0, 1, 2, 3]

    q.popleft()
    assert list(q) == [0, 1, 2, 3]


class Stack(object):
    def __init__(self):
        self.deque = Deque()

    def push(self, value):
        return self.deque.append(value)

    def pop(self):
        return self.deque.pop()

    def __len__(self):
        return len(self.deque)

    def is_empty(self):
        return len(self) == 0


def test_stack():
    s = Stack()
    for i in range(5):
        s.push(i)

    assert len(s) == 5

    assert s.pop() == 4
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() == 0

    assert len(s) == 0

    assert s.is_empty() is True

    import pytest
    with pytest.raises(EmptyError) as excinfo:
        s.pop()

    assert 'empty' in str(excinfo.value)


