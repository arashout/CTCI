from typing import Any
from algo_problems.utils.linked_list import SinglyNode, parse, head_to_linked_list
from algo_problems.utils.testing import Solution, Test


def partition(head: SinglyNode, x: Any):
    if head is None or head.next is None:
        return head

    slow = head
    fast = head.next

    while slow is not None:
        # Need to swap with <= x
        if slow.data >= x:
            while True:
                if fast is None:
                    return
                elif fast.data < x:
                    temp = slow.data
                    slow.data = fast.data
                    fast.data = temp
                    break
                fast = fast.next
        slow = slow.next
        fast = slow.next


def partition2(head: SinglyNode, x: Any):
    left = []
    right = []

    if head is None or head.next is None:
        return head

    node = head
    while node is not None:
        if node.data >= x:
            right.append(node.data)
        else:
            left.append(node.data)
        node = node.next

    node = head
    while node is not None:
        if len(left) != 0:
            node.data = left.pop()
        else:
            node.data = right.pop()
        node = node.next


def partition3(node: SinglyNode, x: Any) -> SinglyNode:
    head = node
    tail = node

    while node is not None:
        next_node = node.next

        if node.data < x:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = next_node

    tail.next = None
    return head_to_linked_list(head)


# t1 = parse('3>5>8>5>10>2>1')
# Solution(
#     partition,
#     [
#         Test(
#             [t1.head, 5],
#             parse('3>2>1>5>10>5>8'),
#             t1
#         )
#     ]
# )

# t1 = parse('3>5>8>5>10>2>1')
# Solution(
#     partition2,
#     [
#         Test(
#             [t1.head, 5],
#             parse('1>2>3>10>5>8>5'),
#             t1
#         )
#     ]
# )

t1 = parse('3>5>8>5>10>2>1')
Solution(
    partition3,
    [
        Test(
            [t1.head, 5],
            parse('1>2>3>5>8>5>10'),
            None
        )
    ]
)
