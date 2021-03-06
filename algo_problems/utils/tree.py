import unittest
import enum
import sys
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
    
    def __eq__(self, other: 'BinaryTreeNode') -> bool:
        if not isinstance(other, BinaryTreeNode):
            return False

        if self is not None and other is not None:
            if self.val == other.val:
                return self.left == other.left and self.right == other.right

            else:
                return False

        elif self is None and other is None:
            return True
        return False


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
        END = ''

    class ValueAction(enum.Enum):
        LEFT_CHILD = 0
        RIGHT_CHILD = 1

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

        while i < len(text) and text[i] not in tokens:
            buffer += text[i]
            i += 1

        if i < len(text):
            if len(buffer) == 0:
                return ReadResult(0, False, Token(text[i]), i)
        
            return ReadResult(int(buffer), True, Token(text[i]), i)
        
        return ReadResult(int(buffer), True, Token.VALUE, i)

    def create_ast(text: str) -> List[ASTNode]:
        ast_nodes = []
        i = 0
        while i < len(text):
            read_result = read_until_token(text, i)
            if read_result.has_value:
                ast_nodes.append(ASTNode(read_result.value, Token.VALUE))
                if read_result.position == len(text):
                    break
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
    parent = None
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
    
    if parent is None:
        return cur_node

    return parent


def is_bst(root: BinaryTreeNode) -> bool:
    def helper(node: BinaryTreeNode, current_min: int, current_max: int) -> bool:
        if node is None:
            return True

        if node.val < current_min or node.val > current_max:
            return False
        
        return helper(node.left, current_min, node.val) and helper(node.right, node.val, current_max)
    
    return helper(root, -sys.maxsize -1, sys.maxsize)


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
    
    def test_eq(self):
        self.assertEqual(parse_tree('10(6(4,7),11)'), parse_tree('10(6(4,7),11)'))
        self.assertNotEqual(parse_tree('10(6(4,7),11)'), parse_tree('10(6(4,7),12)'))

    def test_get_max_depth(self):
        self.assertEqual(2, get_max_depth(self.t1))
        self.assertEqual(2, get_max_depth(self.t2))

        deep_tree = parse_tree('10(11(12(13(14,),),),)')
        self.assertEqual(4, get_max_depth(deep_tree))

    def test_is_bst(self):
        self.assertTrue(is_bst(self.t1))
        self.assertTrue(is_bst(self.t2))
        self.assertFalse(is_bst(parse_tree('3(2(1,4),5)')))
        self.assertTrue(is_bst(parse_tree('3(2(1,),5)')))


if __name__ == '__main__':
    unittest.main()
