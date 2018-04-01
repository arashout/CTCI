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
            
            if node.left is not None:
                text = helper(node.left, text + '(')

            if node.right is not None:
                text = helper(node.right, text + ',') + ')'
            
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
        END = ''

    class ReadResult(NamedTuple):
        value: int
        has_value: bool
        token: Token
        position: int
    
    class HelperResult(NamedTuple):
        parent: BinaryTreeNode
        position: int


    tokens = {t.value:True for t in Token}

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

    def helper(text: str, i: int, parent: BinaryTreeNode) -> HelperResult:
        while True:
            read_result = read_until_token(text, i)
            if read_result.token is Token.LEFT_PARENTHESIS:
                if parent is None:
                    parent = BinaryTreeNode(read_result.value)
                    i = helper(text, read_result.position + 1, parent).position
                else:
                    parent.left = BinaryTreeNode(read_result.value)
                    i = helper(text, read_result.position + 1, parent.left).position

            elif read_result.token is Token.COMMA:
                # Could be case of '),' so we check if it contains value
                if read_result.has_value:
                    parent.left = BinaryTreeNode(read_result.value)
                    i += 1
                else:
                    i += 1

            elif read_result.token is Token.RIGHT_PARENTHESIS:
                parent.right = BinaryTreeNode(read_result.value)
                return HelperResult(parent, read_result.position + 1)
            
            elif read_result.token is Token.END:
                return HelperResult(parent, read_result.position)

            else:
                raise NotImplementedError()
        
        return HelperResult(parent, read_result.position + 1)
        


    tree_text = tree_text.replace(' ', '')
    if len(tree_text) == 0:
        return None

    return helper(tree_text, 0, None).parent


class BinaryTreeTest(unittest.TestCase):
    def setUp(self):
        root = BinaryTreeNode(10)
        root.left = BinaryTreeNode(6)
        root.right = BinaryTreeNode(11)

        root.left.left = BinaryTreeNode(4)
        root.left.right = BinaryTreeNode(7)

        self.tree = root

    def test_str(self):
        self.assertEqual('10(6(4,7),11)',  str(self.tree))

    def test_parse_tree(self):
        parsed_tree = parse_tree( str(self.tree) )
        self.assertEqual(str(self.tree),  str(parsed_tree))
    
    # def test_get_max_depth(self):
    #     tree = parse_tree("1 (23,24)")

if __name__ == '__main__':
    unittest.main()