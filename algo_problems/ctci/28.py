from algo_problems.utils.linked_list import SinglyNode, parse
from algo_problems.utils.testing import Solution, Test

def is_circlular(head: SinglyNode) -> bool:
    if head is None or head.next is None:
        return False

    slow = head
    fast = head.next
    
    while True:
        if slow == fast:
            return True
        elif fast is None or fast.next is None:
            return False
        
        slow = slow.next
        fast = fast.next.next
    
# Circular list
x = SinglyNode(2)
x.next = SinglyNode(1)
x.next.next = SinglyNode(3)
x.next.next.next = x

Solution(
    is_circlular,
    [
        Test(
            [x],
            True,
            None
        ),
        Test(
            [parse('1>2>3>1>2>4').head],
            False,
            None
        )
    ]
)