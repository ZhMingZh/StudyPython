from collections import deque


class BinTreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right


class BinTree(object):
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        """
        通过节点信息构造二叉树
        第一次遍历我们构造 node 节点
        第二次遍历我们给 root 和 孩子赋值
        最后我们用 root 初始化这个类并返回一个对象

        :param node_list:  {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True}
        :return:
        """
        node_dict = {}
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = BinTreeNode(data)
        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
        return cls(root)  # 为啥要cls(root)，不能直接返回root？

    def preorder_trav(self, subtree):
        """先（根）序遍历"""
        if subtree is not None:
            print(subtree.data)
            self.preorder_trav(subtree.left)
            self.preorder_trav(subtree.right)

    def inorder_trav(self, subtree):
        """中(根）序遍历"""
        if subtree is not None:
            self.preorder_trav(subtree.left)
            print(subtree.data)
            self.preorder_trav(subtree.right)

    def postorder_trav(self, subtree):
        """中(根）序遍历"""
        if subtree is not None:
            self.preorder_trav(subtree.left)
            self.preorder_trav(subtree.right)
            print(subtree.data)

    def reverse(self, subtree):
        """反转二叉树"""
        if subtree is not None:
            subtree.left, subtree.right = subtree.right, subtree.left
            self.reverse(subtree.left)
            self.reverse(subtree.right)

    def layer_trav(self, subtree):
        """层序遍历"""
        cur_nodes = [subtree]
        next_nodes = []
        while cur_nodes or next_nodes:
            for node in cur_nodes:
                print(node.data)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            cur_nodes = next_nodes
            next_nodes = []

    def layer_trav_use_queue(self, subtree):
        """利用队列的先进先出的结构，实现层序遍历"""
        q = Queue()
        q.append(subtree)
        while not q.empty():
            cur_node = q.pop()
            print(cur_node.data)
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)


class Queue(object):
    def __init__(self):
        self._items = deque()

    def append(self, value):
        return self._items.append(value)

    def pop(self):
        return self._items.popleft()

    def empty(self):
        return len(self._items) == 0


node_list = [
    {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
    {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
    {'data': 'D', 'left': None, 'right': None, 'is_root': False},
    {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
    {'data': 'H', 'left': None, 'right': None, 'is_root': False},
    {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
    {'data': 'F', 'left': None, 'right': None, 'is_root': False},
    {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
    {'data': 'I', 'left': None, 'right': None, 'is_root': False},
    {'data': 'J', 'left': None, 'right': None, 'is_root': False},
]

# btree 是类还是类的实例；调用了类方法，这里返回的是什么？
btree = BinTree.build_from(node_list)

print('先序遍历'.center(30, '='))
btree.preorder_trav(btree.root)


print('中序遍历'.center(30, '='))
btree.inorder_trav(btree.root)

print('后序遍历'.center(30, '='))
btree.postorder_trav(btree.root)

print('层序遍历'.center(30, '='))
btree.layer_trav(btree.root)

print('层序遍历-使用队列'.center(30, '='))
btree.layer_trav_use_queue(btree.root)
# 反转二叉树
btree.reverse(btree.root)