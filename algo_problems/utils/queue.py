from typing import Any
from algo_problems.utils.linked_list import SinglyNode

class Queue():
    head: SinglyNode
    tail: SinglyNode

    def __init__(self, data: Any = None):
        if data is not None:
            self.head = SinglyNode(data)
            self.tail = self.head
        else:
            self.head = None
            self.tail = None
    

    def __repr__(self):
        string = ''
        node = self.head

        while node is not None:
            string += str(node) + ' > '
            node = node.next

        return string

    def enqueue(self, data: Any):
        new_node = SinglyNode(data)
        if self.head is None:
            self.head = new_node
        else:
            # Change the tail pointer to point to the new node
            self.tail.next = new_node
        # Make the new_node the tail
        self.tail = new_node
    
    def dequeue(self) -> Any:
        if self.head is None:
            raise IndexError('No elements to dequeue')

        old_head = self.head
        self.head = self.head.next
        
        return old_head.data
    
    def is_empty(self) -> bool:
        return self.head is None
    
# q = Queue()
# q.enqueue(3)
# q.enqueue(4)
# print(q)
# q.dequeue()
# q.dequeue()
# q.enqueue(33)
# print(q)