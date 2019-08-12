class BTree_Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BTree(object):
    def __init__(self, root=None):
        self.root = root

    """
    classmethod装饰器可以让方法使用cls来返回或者调用类本身，如以下cls.root用法
    """
    @classmethod
    def Build_from(cls, node_list):
        node_data_dict = {}
        for node_data in node_list:
            data = node_data['data']
            node_data_dict[data] = BTree_Node(data)
        for node_data in node_list:
            data = node_data['data']
            node = node_data_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_data_dict.get(node_data['left'])
            node.right = node_data_dict.get(node_data['right'])
        return cls(root)

    def preorder_trav(self, subtree):
        """
        先（根）序遍历:
        root -> left -> right
        """
        if subtree is not None:
            print(subtree.data)
            self.preorder_trav(subtree.left)
            self.preorder_trav(subtree.right)

    def midorder_trav(self, subtree):
        """
        中序遍历：
        left -> root -> right   
        """
        if subtree is not None:
            self.midorder_trav(subtree.left)
            print(subtree.data)
            self.midorder_trav(subtree.right)

    def backorder_trav(self, subtree):
        """
        后序遍历：
        left -> right ->root     
        """
        if subtree is not None:
            self.backorder_trav(subtree.left)
            self.backorder_trav(subtree.right)
            print(subtree.data)

    def layer_trav(self, subtree):
        """
        层序遍历，思路是：
        从根节点开始按照一层一层的方式遍历节点。 我们可以从根节点开始，之后把所有
        当前层的孩子都按照从左到右的顺序放到一个列表里，下一次遍历所有这些孩子就可以了
        """
        cur_node = [subtree]
        next_nodes = []
        while cur_node or next_nodes:
            for node in cur_node:
                print(node.data)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            cur_node = next_nodes
            next_nodes = []

    def reverse(self, subtree):
        if subtree is not None:
            subtree.left, subtree.right = subtree.right, subtree.left
            self.reverse(subtree.left)
            self.reverse(subtree.right)


node_list = [
    {
        'data': 'A',
        'left': 'B',
        'right': 'C',
        'is_root': True
    },
    {
        'data': 'B',
        'left': 'D',
        'right': 'E',
        'is_root': False
    },
    {
        'data': 'D',
        'left': None,
        'right': None,
        'is_root': False
    },
    {
        'data': 'E',
        'left': 'H',
        'right': None,
        'is_root': False
    },
    {
        'data': 'H',
        'left': None,
        'right': None,
        'is_root': False
    },
    {
        'data': 'C',
        'left': 'F',
        'right': 'G',
        'is_root': False
    },
    {
        'data': 'F',
        'left': None,
        'right': None,
        'is_root': False
    },
    {
        'data': 'G',
        'left': 'I',
        'right': 'J',
        'is_root': False
    },
    {
        'data': 'I',
        'left': None,
        'right': None,
        'is_root': False
    },
    {
        'data': 'J',
        'left': None,
        'right': None,
        'is_root': False
    },
]

btree = BTree.Build_from(node_list)
print("preorder_trav: ")
btree.preorder_trav(btree.root)
print("midorder_trav:")
btree.midorder_trav(btree.root)
print("backorder_trav:")
btree.backorder_trav(btree.root)
print("layer_trav")
btree.layer_trav(btree.root)
