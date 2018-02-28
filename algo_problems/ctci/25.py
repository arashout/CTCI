from algo_problems.utils.linked_list import SinglyNode, parse
from algo_problems.utils.testing import Solution, Test

def linked_list_to_num(head: SinglyNode, base = 10) -> int:
    power = 0
    num = 0
    while head is not None:
        num += head.data * base ** power
        power += 1
        head = head.next
    return num

def num_to_linked_list(num: int, base = 10) -> SinglyNode:
    head = None
    cur = None
    
    while num != 0:
        data = num % base
        if head is None:
            head = SinglyNode(data)
            cur = head
        else:
            cur.next = SinglyNode(data)
            cur = cur.next
        num = num // base
    
    return head

def sum_linked_list(a: SinglyNode, b: SinglyNode) -> SinglyNode:
    total = linked_list_to_num(a) + linked_list_to_num(b)
    return num_to_linked_list(total)

Solution(
    sum_linked_list,
    [
        Test(
            [parse('1>2>3').head, parse('4>5>6').head],
            parse('5>7>9').head,
            None
        )
    ]
)

def add_lists(a: SinglyNode, b: SinglyNode, carry = 0) -> SinglyNode:
    result = carry

    if a is None and b is None:
        if result != 0:
            return SinglyNode(carry)
        return None

    elif a is not None and b is not None:
        result += a.data + b.data
    
    elif a is not None:
        result += a.data
    
    else:
        result += b.data

    if result >= 10:
        carry = 1
        result = result % 10
    else:
        carry = 0

    c = SinglyNode(result)
    c.next = add_lists(a.next, b.next, carry)
    return c


Solution(
    add_lists,
    [
        # Test(
        #     [parse('1>2>3').head, parse('4>5>6').head],
        #     parse('5>7>9').head,
        #     None
        # ),
        Test(
            [parse('1>2>9').head, parse('4>5>6').head],
            parse('5>7>5>1').head,
            None
        )
    ]
)