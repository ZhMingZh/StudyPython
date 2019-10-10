"""
二叉查找树(Binary Search Tree, BST)

二叉查找树是这样一种二叉树结构，它的每个节点包含一个 key 和它附带的数据，对于每个内部节点 V：
所有 key 小于 V 的都被存储在 V 的左子树
所有 key 大于 V 的都存储在 V 的右子树

查找
     如何查找一个指定的节点呢，根据定义我们知道每个内部节点左子树的 key 都比它小，右子树的 key 都比它大，所以 对于带查找的节点 search_key，
     从根节点开始，如果 search_key 大于当前 key，就去右子树查找，否则去左子树查找。 一直到当前节点是 None 了说明没找到对应 key。
"""


class BSTNode(object):
    def __init__(self, key, value, left=None, right=None):
        self.key, self.value, self.left, self.right = key, value, left, right


class BST(object):
    def __init__(self, root=None):
        self.root = root

    @classmethod
    def build_from(cls, node_list):
        cls.size = 0
        key_to_value_dict = {}
        for node_dict in node_list:
            key = node_dict['key']
            key_to_value_dict[key] = BSTNode(key, value=key)  # 这里暂时用key代替value

        for node_dict in node_list:
            key = node_dict['key']
            node = key_to_value_dict[key]
            if node_dict['is_root']:
                root = node
            node.left = key_to_value_dict.get(node_dict['left'])
            node.right = key_to_value_dict.get(node_dict['right'])
            cls.size += 1
        return cls(root)

    def _bst_search(self, subtree, key):
        if subtree is None:  # 没找到
            return None
        elif key < subtree.key:
            return self._bst_search(subtree.left, key)
        elif key > subtree.key:
            return self._bst_search(subtree.right, key)
        else:
            return subtree

    def get(self, key, default=None):
        node = self._bst_search(self.root, key)
        if node is None:
            return default
        else:
            return node.value

    def _bst_min_node(self, subtree):
        """其实还按照其定义，最小值就一直向着左子树找，最大值一直向右子树找，递归查找就行。"""
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self._bst_min_node(subtree.left)

    def bst_min(self):
        node = self._bst_min_node(self.root)
        return node.value if node else None

    def _bst_max_node(self, subtree):
        if subtree is None:
            return None
        elif subtree.right is None:
            return subtree
        else:
            return self._bst_max_node(subtree.right)

    def bst_max(self):
        node = self._bst_max_node(self.root)
        return node.value if node else None

    def _bst_insert(self, subtree, key, value):
        """"插入并返回根节点"""
        if subtree is None:
            subtree = BSTNode(key, value)
        elif key < subtree.key:
            return self._bst_insert(subtree.left, key, value)
        elif key > subtree.key:
            return self._bst_insert(subtree.right, key, value)
        return subtree

    def add(self, key, value):
        node = self._bst_search(self.root, key)
        if node is not None:
            node.value = value
            return False
        else:
            self.root = self._bst_insert(self.root, key, value)
            self.size += 1
            return True

    def _bst_remove(self, subtree, key):
        """删除节点并返回根节点"""
        if subtree is None:
            return None
        elif key < subtree.key:
            subtree.left = self._bst_remove(subtree.left, key)
            return subtree
        elif key > subtree.key:
            subtree.right = self._bst_remove(subtree.right, key)
        else:  # 找到了要删除的节点
            if subtree.left is None and subtree.right is None:  # 叶节点
                return None
            elif subtree.left is None or subtree.right is None:  # 只有一个孩子
                if subtree.left is not None:
                    return subtree.left
                else:
                    return subtree.right
            else:  # 俩孩子 寻找后继节点，并从待删除节点的右子树删除后继节点
                successor_node = self._bst_min_node(subtree.right)
                subtree.key, subtree.value = successor_node.key, successor_node.value
                subtree.right = self._bst_remove(subtree.right, successor_node.value)
                return subtree

    def remove(self, key):
        # assert key in self
        self.size -= 1
        return self._bst_remove(self.root, key)


NODE_LIST = [
                {'key': 60, 'left': 12, 'right': 90, 'is_root': True},
                {'key': 12, 'left': 4, 'right': 41, 'is_root': False},
                {'key': 4, 'left': 1, 'right': None, 'is_root': False},
                {'key': 1, 'left': None, 'right': None, 'is_root': False},
                {'key': 41, 'left': 29, 'right': None, 'is_root': False},
                {'key': 29, 'left': 23, 'right': 37, 'is_root': False},
                {'key': 23, 'left': None, 'right': None, 'is_root': False},
                {'key': 37, 'left': None, 'right': None, 'is_root': False},
                {'key': 90, 'left': 71, 'right': 100, 'is_root': False},
                {'key': 71, 'left': None, 'right': 84, 'is_root': False},
                {'key': 100, 'left': None, 'right': None, 'is_root': False},
                {'key': 84, 'left': None, 'right': None, 'is_root': False},
            ]


def test_bst():
    bst = BST.build_from(NODE_LIST)
    assert bst.get(41) == 41
    assert bst.bst_min() == 1
    assert bst.bst_max() == 100

    bst.add(120, 120)
    assert bst.bst_max() == 120
    assert bst.remove(800) is None