from typing import NamedTuple, Any

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

class SinglyLinkedList():
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
