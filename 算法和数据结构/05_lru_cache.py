import time


class Node(object):
    def __init__(self, prev=None, next=None, key=None, value=None):
        self.prev, self.next, self.key, self.value = prev, next, key, value


class CircularDoubleLinkedList(object):
    def __init__(self):
        node = Node()
        node.prev, node.next = node, node
        self.root = node

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, node):
        tailnode = self.tailnode()
        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node

    def remove(self, node):
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev


class LRUCache(object):
    def __init__(self, maxsize=32):
        self.maxsize = maxsize
        self.cache = {}
        self.access = CircularDoubleLinkedList()
        self.isfull = len(self.cache) >= self.maxsize

    def __call__(self, func):
        def wrapper(n):
            cachenode = self.cache.get(n)
            if cachenode is not None:  # hit
                self.access.remove(cachenode)
                self.access.append(cachenode)
                return cachenode.value
            else:
                value = func(n)
                if not self.isfull:  # miss
                    tailnode = self.access.tailnode()
                    newnode = Node(tailnode, self.access.root, n, value)
                    self.cache[n] = newnode
                    self.access.append(newnode)

                    self.isfull = len(self.cache) >= self.maxsize
                else:  # full
                    lru_node = self.access.headnode()

                    del self.cache[lru_node.key]
                    self.access.remove(lru_node)

                    tailnode = self.access.tailnode()
                    newnode = Node(tailnode, self.access.root, n, value)
                    self.cache[n] = newnode
                    self.access.append(newnode)
                return value
        return wrapper


def cache(func):
    data = {}

    def wrapper(n):
        if n in data:
            return data[n]
        else:
            res = func(n)
            data[n] = res
            return res
    return wrapper


@LRUCache(50)
def fib(n):
    """斐波那契数列-LRUCache"""
    if n <= 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


@cache
def fib2(n):
    """斐波那契数列-字典装饰器（没考虑空间问题）"""
    if n <= 1:
        return n
    else:
        return fib2(n-1) + fib2(n-2)


def fib3(n):
    """斐波那契数列-字典装饰器（没考虑空间问题）"""
    if n <= 2:
        return n
    else:
        return fib3(n-1) + fib3(n-2)


def test():
    start = time.time()
    for i in range(50):
        print(fib(i))
    print(time.time() - start)
    # 0.0007722377777099609


if __name__ == '__main__':
    test()

    # start = time.time()
    # for i in range(5000):
    #     fib2(i)
    # print(time.time() - start)
    # print('=' * 50)
    #
    # start = time.time()
    # for i in range(50):
    #     fib3(i)
    # print(time.time() - start)