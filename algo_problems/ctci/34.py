from typing import Any

from algo_problems.utils.testing import command_test_loop, Command

class QueueWithStacks:
    def __init__(self):
        self.stack_recent = []
        self.stack_old = []
    
    def __len__(self):
        return len(self.stack_recent) + len(self.stack_old)

    def shift_stacks(self):
        while len(self.stack_recent) != 0:
            self.stack_old.append(self.stack_recent.pop())

    def enqueue(self, data: Any):
        self.stack_recent.append(data)
    
    def deque(self) -> Any:
        if len(self) == 0:
            raise IndexError('Nothing to deque')

        self.shift_stacks()

        return self.stack_old.pop()


if __name__ == '__main__':
    qws = QueueWithStacks()
    commands = {
        '0': Command(qws.enqueue, 1, 'enqueue'),
        '1': Command(lambda: print(qws.deque()), 0, 'deque')
    }
    command_test_loop(commands, lambda: print())