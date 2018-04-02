import unittest
import enum

from typing import List, Tuple, NamedTuple


class BinaryTreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: BinaryTreeNode = None
        self.right: BinaryTreeNode = None

    def __str__(self):
        """ Returns a pre-order text representation of the tree """
        def helper(node: BinaryTreeNode, text: str) -> str:
            if node is not None:
                text += str(node.val)

            if node.left is not None or node.right is not None:
                text += '('
                if node.left is not None:
                    text = helper(node.left, text)
                text += ','
                if node.right is not None:
                    text = helper(node.right, text)
                text += ')'

            return text

        return helper(self, '')

    def __repr__(self):
        return str(self)


def get_max_depth(root: BinaryTreeNode):
    def helper(node: BinaryTreeNode, d: int) -> int:
        if node.left is not None and node.right is not None:
            return max([helper(node.left, d+1), helper(node.right, d+1)])
        elif node.left is not None:
            return helper(node.left, d+1)
        elif node.right is not None:
            return helper(node.right, d+1)
        else:
            return d

    return helper(root, 0)


def parse_tree(tree_text: str) -> BinaryTreeNode:
    class Token(enum.Enum):
        LEFT_PARENTHESIS = '('
        RIGHT_PARENTHESIS = ')'
        COMMA = ','
        VALUE = 'value'

    class ValueAction(enum.Enum):
        LEFT_CHILD = 0
        RIGHT_CHILD = 1
        PARENT = 2

    class ReadResult(NamedTuple):
        value: int
        has_value: bool
        token: Token
        position: int

    class ASTNode(NamedTuple):
        value: int
        token: Token

    tokens = {t.value: True for t in Token}

    def read_until_token(text: str, i: int) -> ReadResult:
        buffer = ''
        if i >= len(text):
            return ReadResult(0, False, Token.END, i)

        while text[i] not in tokens:
            buffer += text[i]
            i += 1

        if len(buffer) == 0:
            return ReadResult(0, False, Token(text[i]), i)

        return ReadResult(int(buffer), True, Token(text[i]), i)

    def create_ast(text: str) -> List[ASTNode]:
        ast_nodes = []
        i = 0
        while i < len(text):
            read_result = read_until_token(text, i)
            if read_result.has_value:
                ast_nodes.append(ASTNode(read_result.value, Token.VALUE))
                ast_nodes.append(ASTNode(0, read_result.token))
            else:
                ast_nodes.append(ASTNode(0, read_result.token))
            i = read_result.position + 1

        return ast_nodes

    tree_text = tree_text.replace(' ', '')
    if len(tree_text) == 0:
        return None
    ast_nodes = create_ast(tree_text)
    # First node is always the root
    if ast_nodes[0].token is not Token.VALUE:
        raise ValueError('Root should be first node')

    # Stack to replace recursion
    s = []
    cur_node = BinaryTreeNode(ast_nodes[0].value)
    cur_action = None
    i = 1
    while i < len(ast_nodes):
        ast_node = ast_nodes[i]
        if ast_node.token is Token.LEFT_PARENTHESIS:
            s.append(cur_node)
            cur_action = ValueAction.LEFT_CHILD

        elif ast_node.token is Token.VALUE:
            cur_node = BinaryTreeNode(ast_node.value)

            if cur_action is ValueAction.LEFT_CHILD:
                s[-1].left = cur_node
            elif cur_action is ValueAction.RIGHT_CHILD:
                s[-1].right = cur_node

        elif ast_node.token is Token.COMMA:
            cur_action = ValueAction.RIGHT_CHILD

        elif ast_node.token is Token.RIGHT_PARENTHESIS:
            # Last pop will be root!
            parent = s.pop()

        i += 1
    return parent


def is_bst(node: BinaryTreeNode) -> bool:
    if node is None:
        return True

    if node.left is not None and node.left.val > node.val:
        return False

    if node.right is not None and node.right.val < node.val:
        return False

    if not is_bst(node.left) or not is_bst(node.right):
        return False

    return True


class BinaryTreeTest(unittest.TestCase):
    def setUp(self):
        root = BinaryTreeNode(10)
        root.left = BinaryTreeNode(6)
        root.right = BinaryTreeNode(11)
        root.left.left = BinaryTreeNode(4)
        root.left.right = BinaryTreeNode(7)
        self.t1 = root

        root = BinaryTreeNode(10)
        root.left = BinaryTreeNode(6)
        root.right = BinaryTreeNode(11)
        root.left.left = BinaryTreeNode(4)
        root.right.right = BinaryTreeNode(12)
        self.t2 = root

    def test_str(self):
        self.assertEqual('10(6(4,7),11)',  str(self.t1))
        self.assertEqual('10(6(4,),11(,12))', str(self.t2))

    def test_parse_tree(self):
        """Parsed tree should be same as original"""
        self.assertEqual(str(self.t1),  str(parse_tree(str(self.t1))))
        self.assertEqual(str(self.t2),  str(parse_tree(str(self.t2))))

    def test_get_max_depth(self):
        self.assertEqual(2, get_max_depth(self.t1))
        self.assertEqual(2, get_max_depth(self.t2))

        deep_tree = parse_tree('10(11(12(13(14,),),),)')
        self.assertEqual(4, get_max_depth(deep_tree))

    def test_is_bst(self):
        self.assertTrue(is_bst(self.t1))
        self.assertTrue(is_bst(self.t2))

        not_bst = parse_tree('10(11(12(13(14,),),),)')
        self.assertFalse(is_bst(not_bst))


if __name__ == '__main__':
    unittest.main()
