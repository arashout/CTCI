from algo_problems.utils.linked_list import SinglyNode, parse
from algo_problems.utils.testing import Solution, Test

def is_intersecting(a: SinglyNode, b: SinglyNode) -> bool:
    seen = {}
    node = a
    while node is not None:
        seen[node] = True
        node = node.next
    
    node = b
    while node is not None:
        if node in seen:
            return True
        node = node.next
    
    return False

def get_intersection(head_a: SinglyNode, head_b: SinglyNode) -> (int, int):
    class Result:
        def __init__(
            self, 
            a: SinglyNode, 
            b: SinglyNode, 
            has_intersection: bool,
            j: int,
            k: int
        ):
            self.a = a
            self.b = b
            self.has_intersection = has_intersection
            self.j = j
            self.k = k

    def helper(a: SinglyNode, b: SinglyNode, j: int, k: int) -> Result:
        res = None
        if a is None or b is None:
            return Result(a, b, False, -1, -1)
        elif a.next is None and b.next is None:
            return Result(a, b, a == b, j, k)
        elif a.next is None:
            res = helper(a, b.next, j, k+1)
        elif b.next is None:
            res = helper(a.next, b, j+1, k)
        else:
            res = helper(a.next, b.next, j+1, k+1)
        
        if res.has_intersection:
            if a == b:
                res.j = j
                res.k = k

        return res
    
    final = helper(head_a, head_b, 0, 0)
    return (final.j, final.k)

# The method in the book involved looking at differences in lengths 
# Starting the pointers at same point by using an offset and comparing

# TODO: Figure out how to test
