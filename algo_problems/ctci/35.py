from algo_problems.utils.testing import Solution, Test

# NOTE: Can only use one additional stack

def sort_stack(s: list):
    temp_stack = []
    while len(s) != 0:
        temp = s.pop()
        while len(temp_stack) !=0 and temp_stack[-1] > temp:
            s.append(temp_stack.pop())
        temp_stack.append(temp)
    
    while len(temp_stack) != 0:
        s.append(temp_stack.pop())
    
s1 = [2, 3, 1, 5]
Solution(
    sort_stack,
    [
        Test(
            [s1],
            [5, 3, 2, 1],
            s1
        )
    ]
)
