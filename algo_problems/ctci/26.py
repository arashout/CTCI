from algo_problems.utils.linked_list import SinglyNode, parse
from algo_problems.utils.testing import Solution, Test

def get_length(head: SinglyNode) -> int:
    length = 0
    while head is not None:
        length += 1
        head = head.next

    return length

def is_palindrome(head: SinglyNode) -> bool:
    n = get_length(head)
    if n <= 1:
        return True

    front_stack = []
    end_front = n//2
    node = head
    i = 0
    while i < end_front:
        front_stack.append(node.data)
        node = node.next
        i += 1
    
    if n % 2 != 0:
        node = node.next

    while len(front_stack) != 0:
        data = front_stack.pop()
        if node.data != data:
            return False
        node = node.next

    return True

test_table =   [
        Test(
            [parse('1>2>3>5>3>2>1').head],
            True,
            None
        ),
                Test(
            [parse('1>2>3>3>2>1').head],
            True,
            None
        )
    ]
Solution(
    is_palindrome,
    test_table
)    

class Result:
    def __init__(self, node: SinglyNode = None, match: bool = False):
        self.node = node
        self.match = match


def is_palindrome_rec(head: SinglyNode) -> bool:
    mid = get_length(head)

    def helper(node: SinglyNode, length: int) -> Result:
        # node is None is the case when you are given an empty list
        if node is None or length <= 0:
            return Result(node, True)
        elif length == 1:
            return Result(node.next, True)
        
        res = helper(node.next, length - 2)

        if not res.match or res.node is None:
            return res
        
        res.match = (res.node.data == node.data)
        res.node = res.node.next

        return res
    
    final = helper(head, mid)
    return final.match

Solution(
    is_palindrome_rec,
    test_table
)    

