from typing import Any
from algo_problems.utils.linked_list import SinglyNode


class MinStackNode:
    def __init__(self, data: Any, min_data=None):
        self.data = data
        self.pointer = None
        self.min_data = min_data


class MinStack:
    def __init__(self):
        self.top = None

    def push(self, data: Any):
        if self.top is None:
            self.top = MinStackNode(data, data)
        else:
            new_min = data if self.top.min_data > data else self.top.min_data
            new_node = MinStackNode(data, new_min)
            new_node.pointer = self.top
            self.top = new_node

    def pop(self) -> Any:
        if self.top is None:
            raise IndexError('No elements on stack')
        else:
            temp_node = self.top
            self.top = temp_node.pointer
            return temp_node

    def get_min(self) -> Any:
        if self.top is None:
            raise IndexError('No elements on stack')
        else:
            return self.top.min_data

    def __str__(self) -> str:
        full_string = ''
        node = self.top
        while node is not None:
            full_string += '<{0}'.format(node.data)
            node = node.pointer
        return full_string

class MinStack2:
    def __init__(self):
        self.top = None
        self.min_stack = []

    def push(self, data: Any):
        if self.top is None:
            self.top = SinglyNode(data)
            self.min_stack.append(data)
        else:
            if data <= self.min_stack[-1]:
                self.min_stack.append(data)
            new_node = SinglyNode(data)
            new_node.next = self.top
            self.top = new_node

    def pop(self) -> Any:
        if self.top is None:
            raise IndexError('No elements on stack')
        else:
            temp_node = self.top
            self.top = temp_node.next

            if temp_node.data == self.min_stack[-1]:
                self.min_stack.pop()

            return temp_node

    def get_min(self) -> Any:
        if self.top is None:
            raise IndexError('No elements on stack')
        else:
            return self.min_stack[-1]

    def __str__(self) -> str:
        full_string = ''
        node = self.top
        while node is not None:
            full_string += '<{0}'.format(node.data)
            node = node.next
        return full_string

if __name__ == '__main__':
    s = MinStack2()
    while True:
        c = input('1: Push\n2: Pop\n3: Min\n')
        if c == '1':
            d = input()
            s.push(int(d))
            print(s)
        elif c == '2':
            print(s.pop())
            print(s)
        elif c == '3':
            print(s.get_min())
            print(s)
        else:
            print(s)
