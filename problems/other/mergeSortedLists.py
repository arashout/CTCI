from Testing import Solution, Test
from LinkedList import SinglyLinkedList, SinglyNode, parse


def merge_sorted_lists(a: list, b: list) -> list:
    n = len(a)
    m = len(b)

    # Pre-allocate list
    c = [None] * (m + n)

    i = 0
    j = 0
    k = 0

    while i < n or j < m:
        if i == n:
            c[k] = b[j]
            j += 1
        elif j == m:
            c[k] = a[i]
            i += 1
        else:
            if a[i] < b[j]:
                c[k] = a[i]
                i += 1
            else:
                c[k] = b[j]
                j += 1
        k += 1
    return c


Solution(
    merge_sorted_lists,
    [
        Test([[1, 3, 5], [1, 2, 5, 7]], [1, 1, 2, 3, 5, 5, 7]),
        Test([[], [1, 2, 5]], [1, 2, 5]),
    ]
)


def merge_sorted_linked_lists(a: SinglyLinkedList, b: SinglyLinkedList) -> SinglyLinkedList:
    def rec(i: SinglyNode, j: SinglyNode, k: SinglyNode):
        if i is None and j is None:
            return
        else:
            if i is None:
                k.next = j
            elif j is None:
                k.next = i
            else:
                if i.data < j.data:
                    k.next = SinglyNode(i.data)
                    rec(i.next, j, k.next)
                else:
                    k.next = SinglyNode(j.data)
                    rec(i, j.next, k.next)

    c = SinglyLinkedList(SinglyNode(None))
    rec(a.head, b.head, c.head)
    c.pop_front()
    return c
        
def merge_test_helper(a: SinglyLinkedList, b: SinglyLinkedList) -> str:
    return str(merge_sorted_linked_lists(a, b))

Solution(
    merge_test_helper,
    [
        Test([parse('1 > 3 > 5'), parse('1 > 5 > 7')], '1 > 1 > 3 > 5 > 5 > 7 > '),
        Test([parse('1 > 1'), parse('')], '1 > 1 > ')
    ]
)
