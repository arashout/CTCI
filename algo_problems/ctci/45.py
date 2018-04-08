from algo_problems.utils.tree import BinaryTreeNode, parse_tree
from algo_problems.utils.testing import Solution, Test
from typing import NamedTuple
import sys

def validate_BST(root: BinaryTreeNode) -> bool:
    def helper(node: BinaryTreeNode, cur_min: int, cur_max: int) -> bool:
        if node is None:
            return True
        
        if node.val < cur_min or node.val > cur_max:
            return False
        
        return helper(node.left, cur_min, node.val) and helper(node.right, node.val, cur_max)

    return helper(root, -sys.maxsize, sys.maxsize)