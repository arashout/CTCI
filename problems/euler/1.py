from typing import List

def sum_multiples(list_nums: List[int], n: int) -> int :
    total = 0
    for i in range(n):
        if any(i % j == 0 for j in list_nums):
            total += i
    return total

print(sum_multiples([3,5], 1000))