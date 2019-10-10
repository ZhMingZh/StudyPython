class Node(object):
    """节点"""
    def __init__(self, value=None, next=None):  # 根结点默认值为None
        self.value = value
        self.next = next

    def __str__(self):
        return '<Node: value: {}, next: {}>'.format(self.value, self.next)

    __repr__ = __str__


class LinkedList(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        if self.maxsize is not None and len(self) > self.length:
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
        if self.maxsize is not None and len(self) > self.length:
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
        if curnode is not None:
            yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def remove(self, value):
        """删除包含包含值的一个节点，将其一个前节点的next指向被查询的节点的下一个即可"""
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
        """反转链表, 没理解"""
        curnode = self.root.next
        self.tailnode = curnode
        prevnode = None

        while curnode:
            nextcode = curnode.next
            curnode.next = prevnode

            if nextcode is None:
                self.root.next = curnode

            prevnode = curnode
            curnode = nextcode


# ============================================
# 下边是队列 Queue 的实现
# ============================================
class FullError(Exception):
    pass


class EmptyError(Exception):
    pass


class Queue(object):
    """FIFO 先进先出"""
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._item_linked_list = LinkedList()

    def __len__(self):
        return len(self._item_linked_list)

    def push(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise FullError('queue full')
        self._item_linked_list.append(value)

    def pop(self):
        if len(self) <= 0:
            raise EmptyError('empty queue')
        return self._item_linked_list.popleft()


def test_queue():
    q = Queue()
    q.push(0)
    q.push(1)
    q.push(2)

    assert len(q) == 3

    q.pop()
    q.pop()
    q.pop()

    assert len(q) == 0

    import pytest
    with pytest.raises(EmptyError) as excinfo:
        q.pop()
    assert 'empty' in str(excinfo.value)

    with pytest.raises(FullError) as excinfo:
        q.push(10)

    assert 'full' in str(excinfo.value)




