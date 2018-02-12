from problems.utils.testing import Solution, Test
from typing import NamedTuple, Any
from abc import ABC


class Node(NamedTuple):
    data: Any

    def __repr__(self):
        return str(self.data)

    def __str__(self):
        return str(self.data)


class SinglyNode(Node):
    next: Node

    def __new__(cls, node: Node):
        self = super(SinglyNode, cls).__new__(cls, node)
        self.next = None
        return self


class DoublyNode(Node):
    next: Node
    prev: Node


class LinkedList(ABC):
    def __init__(self, head: Node):
        self.head = head


class SinglyLinkedList(LinkedList):
    head: SinglyNode

    def __init__(self, head: SinglyNode):
        self.head = head

    def __repr__(self):
        string = ''
        node = self.head

        while node is not None:
            string += str(node) + ' > '
            node = node.next

        return string

    def prepend(self, data: Any):
        if self.h ead is None:
            self.head = SinglyNode(data)
        else:
            temp = self.head
            self.head = SinglyNode(data)
            self.head.next = temp

    def pop_front(self) -> Any:
        if self.head is None:
            # Maybe should raise error?
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def reverse(self):
        if self.head is None or self.head.next is None:
            return self.head

        prev = None
        cur = self.head

        while cur is not None:
            temp = cur.next
            cur.next = prev

            prev = cur
            cur = temp

        return


def parse(string: str, is_doubly_linked: bool = False) -> LinkedList:
    if is_doubly_linked:
        raise NotImplementedError
    else:
        sll = SinglyLinkedList(None)
        split_string = string.replace(' ', '').split('>')
        split_string = list(filter(None, split_string))

        # Assume they are ints ->
        # Could handle generics by having a parse_type method for each type
        for i in range(len(split_string) - 1, -1, -1):
            data = int(split_string[i])
            sll.prepend(data)
        return sll
