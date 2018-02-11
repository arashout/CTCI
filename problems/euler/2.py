def fib(n: int, memo={}):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        if n in memo:
            return memo[n]
        
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]

def sum_fib(max_num: int) -> int:
    total = 0
    i = 0
    memo = {}
    while total < max_num:
        val = fib(i, memo)
        if val % 2 == 0:
            total += val
        i += 1
    return total

print(sum_fib(4*10**6))