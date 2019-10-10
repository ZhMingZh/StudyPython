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
        curnode = self.root.next  # 头节点
        while curnode.next is not self.root:  # 判断是不是只有一个节点
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
        curnode = self.root.prev  # 尾节点
        # self.root 是根节点
        while curnode.prev is not self.root:  # 判断是不是只有一个节点
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


def test_double_link_list():
    dll = CircularDoubleLinkedList()
    assert len(dll) == 0

    dll.append(0)
    dll.append(1)
    dll.append(2)

    assert list(dll) == [0, 1, 2]

    assert [node.value for node in dll.iter_node()] == [0, 1, 2]
    assert [node.value for node in dll.iter_node_reverse()] == [2, 1, 0]

    headnode = dll.headnode()
    assert headnode.value == 0
    dll.remove(headnode)
    assert len(dll) == 2
    assert [node.value for node in dll.iter_node()] == [1, 2]

    dll.appendleft(0)
    assert [node.value for node in dll.iter_node()] == [0, 1, 2]

    dll.insert(1, 4)
    assert list(dll) == [0, 4, 1, 2]

    dll.insert(2, 5)
    assert list(dll) == [0, 4, 1, 5, 2]

    dll.insert(0, 6)
    assert list(dll) == [6, 0, 4, 1, 5, 2]


if __name__ == '__main__':
    test_double_link_list()