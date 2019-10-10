from collections import deque


graph = {
    'A': ['B', 'F'],
    'B': ['C', 'I', 'G'],
    'C': ['B', 'I', 'D'],
    'D': ['C', 'I', 'G', 'H', 'E'],
    'E': ['D', 'H', 'F'],
    'F': ['A', 'G', 'E'],
    'G': ['B', 'F', 'H', 'D'],
    'H': ['G', 'D', 'E'],
    'I': ['B', 'C', 'D'],
}


class Queue(object):
    """先进先出"""
    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.popleft()

    def __len__(self):
        return len(self._deque)


def bfs(graph, start):
    """BFS 广度优先遍历"""
    search_deque = Queue()
    search_deque.push(start)
    searched = set()
    while search_deque:  # 队列不为空就继续
        cur_node = search_deque.pop()
        if cur_node not in searched:
            yield cur_node
            searched.add(cur_node)
            for node in graph[cur_node]:
                search_deque.push(node)


DFS_SEARCHED = set()


class Stack(object):
    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.pop()

    def __len__(self):
        return len(self._deque)


def dfs(graph, start):
    """DFS 深度优先遍历"""
    # if start not in DFS_SEARCHED:
    #     print(start)
    #     DFS_SEARCHED.add(start)
    # for node in graph[start]:
    #     if node not in DFS_SEARCHED:
    #         dfs(graph, node)
    stack = Stack()
    stack.push(start)
    searched = set()
    while stack:
        cur_node = stack.pop()
        if cur_node not in searched:
            print(cur_node)
            searched.add(cur_node)
            for node in reversed(graph[cur_node]):
                stack.push(node)


def dfs1(graph, start):
    """DFS 深度优先遍历"""
    # if start not in DFS_SEARCHED:
    #     print(start)
    #     DFS_SEARCHED.add(start)
    # for node in graph[start]:
    #     if node not in DFS_SEARCHED:
    #         dfs(graph, node)
    stack = Stack()
    stack.push(start)
    searched = set()
    while stack:
        cur_node = stack.pop()
        if cur_node not in searched:
            print(cur_node)
            searched.add(cur_node)
            for node in graph[cur_node]:
                stack.push(node)


print('bfs:')
for node in bfs(graph, 'A'):
    print(node)

print('dfs:')
dfs(graph, 'A')

print('df1:')
dfs1(graph, 'A')