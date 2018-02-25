from algo_problems.utils.linked_list import SinglyNode, parse
from algo_problems.utils.testing import Solution, Test

def delete_middle(node: SinglyNode):
    while node.next is not None:
        node.data = node.next.data

        if node.next.next is None:
            node.next = None
            break
        
        node = node.next

t1 = parse('1>2>3>4>5')
Solution(
    delete_middle,
    [
        Test(
            [t1.k_th(2)],
            parse('1>2>4>5'),
            t1
        )
    ]
)