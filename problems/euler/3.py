from typing import List

def primes(n: int) -> List[int]:
    p = 2
    e = 1
    primes = []
    while n != 1:
        if n % p == 0:
            n /= p
            e += 1
        else:
            if e != 1:
                primes.append(p)
                e = 1
            p += 1
    primes.append(p)
    return primes

print(max(primes(600851475143)))     
