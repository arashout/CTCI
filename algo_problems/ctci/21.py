from algo_problems.utils.testing import Test, Solution
from algo_problems.utils.linked_list import SinglyNode, parse

def remove_dups(head: SinglyNode) -> SinglyNode:
    if head is None:
        return
    
    seen = {}
    prev = None
    node = head

    while node is not None:
        if node.data in seen:
            prev.next = node.next
        else:
            seen[node.data] = True
            prev = node
        
        node = node.next
    
    return head

def remove_dups_no_buffer(head: SinglyNode) -> SinglyNode:
    current = head
    
    if head is None:
        return head

    while current is not None:
        runner = current
        
        while runner.next is not None:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        
        current = current.next
    return head

Solution(
    remove_dups_no_buffer,
    [
        Test(
            [parse('1>1').head],
            parse('1').head
        ),
        Test(
            [parse('1>2>3>2').head],
            parse('1>2>3').head
        )
    ] 
)
