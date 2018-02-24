from typing import Any
from algo_problems.utils.linked_list import SinglyNode, parse
from algo_problems.utils.queue import Queue
from algo_problems.utils.testing import Solution, Test


def kth_last(head: SinglyNode, k: int) -> Any:
    if head is None:
        return None

    node = head
    k_last = Queue()
    result = None
    count = 0

    while node is not None:
        k_last.enqueue(node.data)
        count += 1

        if count > k:
            result = k_last.dequeue()

        node = node.next

    return result


def kth_last_optimal(head: SinglyNode, k: int) -> Any:
    p1 = head
    p2 = p1
    for _ in range(k):
        if p2 is None:
            return None
        p2 = p2.next

    while True:
        if p2 is None:
            return p1
        p2 = p2.next
        p1 = p1.next


def kth_last_rec(head: SinglyNode, k: int) -> Any:
    class IntWrapper:
        def __init__(self, val: int = 0):
            self.val = val
    
    def helper(helper_head: SinglyNode, k: int, w: IntWrapper) -> SinglyNode:
        if helper_head is None:
            return None

        node = helper(helper_head.next, k, w)
        w.val += 1
        
        if w.val == k:
            return helper_head
        
        return node
    
    return helper(head, k, IntWrapper(val=0))

Solution(
    kth_last_rec,
    [
        Test(
            [parse('1>2>3>4').head, 2],
            SinglyNode(3)
        ),
        Test(
            [parse('1>2>3>4').head, 1],
            SinglyNode(4)
        ),
        Test(
            [parse('1').head, 1],
            SinglyNode(1)
        )
    ]
)
