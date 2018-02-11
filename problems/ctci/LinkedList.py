from typing import NamedTuple, Any

class Node(NamedTuple):
    data: Any

class SinglyNode(Node):
    next: Node
    
    def __init__(self, _data: Any):
        self.data = _data

class DoublyNode(Node):
    next: Node
    prev: Node

class SinglyLinkedList:
    head: SinglyNode

    def __init__(self, _node: SinglyNode):
        self.head = _node