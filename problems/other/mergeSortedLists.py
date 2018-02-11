from Testing import Solution, Test
from LinkedList import SinglyLinkedList, SinglyNode

def mergeSortedLists(a: list, b: list) -> list:
    n = len(a)
    m = len(b)
    
    # Pre-allocate list
    c = [None] * (m+n)

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
    mergeSortedLists,
    [
        Test([ [1,3,5], [1, 2, 5, 7] ], [1, 1, 2, 3, 5, 5, 7]),
        Test([ [], [1, 2, 5] ], [1, 2, 5]),
    ]
)

def mergeSortedLinkedLists(a: SinglyLinkedList):
    print(a)

mergeSortedLinkedLists(SinglyLinkedList(SinglyNode(4)))
