from algo_problems.utils.testing import Solution, Test
from algo_problems.utils.tree import BinaryTreeNode, is_bst, parse_tree

from typing import List

def create_bst(sorted_list: List[int]) -> BinaryTreeNode:
    def helper(start: int, end: int) -> BinaryTreeNode:
        if start > end:
            return None
        
        mid = (start + end)//2
        node = BinaryTreeNode(sorted_list[mid])
        node.left = helper(start, mid-1)
        node.right = helper(mid+1, end)
        return node
    
    return helper(0, len(sorted_list) - 1)




Solution(
    create_bst,
    [
        Test(
            [
                [1, 2, 3, 4, 5]
            ],
            parse_tree('3(1(,2),4(,5))'),
            None
        )

    ]

)