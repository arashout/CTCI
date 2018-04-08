from algo_problems.utils.testing import Solution, Test
from typing import Any
from abc import ABC


class Node(ABC):
    data: any
    def __repr__(self):
        return 'N: ' + str(self.data)

    def __str__(self):
        return 'N: ' + str(self.data)


class SinglyNode(Node):
    next: 'SinglyNode'
    def __init__(self, data: Any):
        self.data = data
        self.next = None

    def __eq__(self, other: Node):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False


class DoublyNode(ABC):
    def __init__(self, data: Any):
        self.data = data
        self.next = None
        self.prev = None

    def __eq__(self, other: 'DoublyNode'):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False


class LinkedList(ABC):
    def __init__(self, head: Node):
        self.head = head


class SinglyLinkedList(LinkedList):
    head: SinglyNode

    def __init__(self, head: SinglyNode = None):
        self.head = head

    def __repr__(self):
        string = ''
        node = self.head

        while node is not None:
            string += str(node) + ' > '
            node = node.next

        return string
    
    def __iter__(self: 'SinglyLinkedList'):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __eq__(self, other: LinkedList):
        """Overrides the default implementation"""
        if isinstance(self, other.__class__):
            return self.__dict__ == other.__dict__
        return False

    def prepend(self, data: Any):
        if self.head is None:
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
    
    def k_th(self, k) -> SinglyNode:
        node = self.head
        for _ in range(k):
            if node is None:
                return None

            node = node.next
        return node

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

def head_to_linked_list(head: SinglyNode) -> SinglyLinkedList:
    sll = SinglyLinkedList()
    temp_list = []
    
    while head is not None:
        temp_list.append(head.data)
        head = head.next
    
    for i in range(len(temp_list)-1, -1, -1):
        sll.prepend(temp_list[i])
    
    return sll

