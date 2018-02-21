from algo_problems.utils.linked_list import SinglyNode

class Queue():
    head: SinglyNode
    tail: SinglyNode

    def __init__(self, node: SinglyNode = None):
        self.head = node
        self.tail = node
    

    def __repr__(self):
        string = ''
        node = self.head

        while node is not None:
            string += str(node) + ' > '
            node = node.next

        return string

    def enqueue(self, node: SinglyNode):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
    
    def dequeue(self) -> SinglyNode:
        if self.head is None:
            raise IndexError('No elements to dequeue')

        old_head = self.head
        self.head = self.head.next
        
        return old_head
    
    def is_empty(self) -> bool:
        return self.head is None

q = Queue(SinglyNode(4))
print(q.is_empty())
q.enqueue(SinglyNode(3))
print(q.dequeue())
print(q.dequeue())
print(q.is_empty())
print(q)

