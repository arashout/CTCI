from algo_problems.utils.tree import BinaryTreeNode, parse_tree
from algo_problems.utils.testing import Solution, Test
from typing import List, NamedTuple

def check_balanced(root: BinaryTreeNode) -> bool:
    class Result(NamedTuple):
        is_balanced: bool
        height: int

    def helper(node: BinaryTreeNode, height: int) -> Result:
        if node is None:
            return Result(True, height)
        l: Result = helper(node.left, height + 1)
        r: Result = helper(node.right, height + 1)

        if not l.is_balanced or not r.is_balanced:
            return Result(False, max(l.height, r.height))
        
        if abs(l.height - r.height) > 1:
            return Result(False, max(l.height, r.height))
        
        return Result(True, max(l.height, r.height))
    
    return helper(root, 0).is_balanced

Solution(
    check_balanced,
    [
        Test(
            [parse_tree('1(2(2,),3(1,))')],
            True,
            None
        ),
        Test(
            [parse_tree('1(2(2,3),3)')],
            True,
            None
        ),
        Test(
            [parse_tree('1(2(2,3(1,2)),3)')],
            False,
            None
        ),
        Test(
            [parse_tree('1(2(1(2,),),3(1(2,),))')],
            False,
            None
        ),
    ]
)