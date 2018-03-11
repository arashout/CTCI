from typing import Any

from algo_problems.utils.testing import command_test_loop, Command

class SetOfStacks:
    def __init__(self, threshold: int):
        self.sos = [ [] ] # Initialized with one stack
        self.threshold = threshold
    
    def push(self, data: Any):
        # Assume we always have one stack in our set
        if len(self.sos[-1]) == self.threshold:
            self.sos.append([data])
        else:
            self.sos[-1].append(data)
    
    def pop(self) -> Any:
        # Ensure we maintain invariant: There is always one stack
        isOnlyStack = len(self.sos) == 1
        if isOnlyStack:
            if len(self.sos[0]) == 0:
                raise IndexError('No more elements on stacks')

        res = self.sos[-1].pop()
        if len(self.sos[-1]) == 0:
            if not isOnlyStack:
                self.sos.pop()
        return res
    
    def pop_at(self, i: int) -> Any:
        # TODO: Implement rollover...
        if ( len(self.sos) - 1 ) < i:
            raise IndexError('No enough stacks to pop from {0} index'.format(i))

        res = self.sos[i].pop()

        return res
            
    
    def __repr__(self) -> str:
        string = ''
        for s in self.sos:
            for d in s:
                string += str(d) + ' '
            string += '->'
        return string

if __name__ == '__main__':
    sos = SetOfStacks(5)
    commands = {
        '0': Command(lambda: sos.pop(), 0),
        '1': Command(sos.push, 1),
    }
    command_test_loop(commands, lambda: print(sos))