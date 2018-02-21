from typing import Any
from algo_problems.utils.linked_list import SinglyNode, parse

def kth_last(head: SinglyNode) -> Any:
    if head is None:
        return None
    
    node = head
    last_k = []

    while node is not None:
        last_k.append(node.data)
        