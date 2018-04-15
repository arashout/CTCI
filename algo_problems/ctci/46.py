from typing import NamedTuple, Any

class BTNodeWithParent(NamedTuple):
    val: Any
    left: 'BTNodeWithParent'
    right: 'BTNodeWithParent'
    parent: 'BTNodeWithParent'
    

def successor(node: BTNodeWithParent) -> BTNodeWithParent:
    if node.right is not None:
        return node.right
    
    cur = node.parent
    while cur is not None:
        if cur.val > node.val:
            return cur
        cur = cur.parent
    return None

