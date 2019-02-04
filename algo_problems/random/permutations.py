from typing import List
def generatePermutations(L: List[str], k: int) -> List[str]:
    def helper(freqs: List[int], _k: int, curString: str, _results: List[str]):
        if _k == 0:
            _results.append(curString)
        else:
            for i in range(len(freqs)):
                if freqs[i] != 0:
                    freqs[i] -= 1
                    helper(freqs, _k - 1, curString + L[i], results)
                    freqs[i] += 1
    results = []
    freqs = [1 for i in L]
    helper(freqs, k, '', results)
    return results

def generateCombinations(L: List[str], k: int) -> List[str]:
    permutations = generatePermutations(L, k)
    s = set()
    for p in permutations:
        s.add(''.join(sorted(p)))
    return list(s)

ps = generatePermutations([str(n) for n in range(1, 5)], 3)
cs = generateCombinations([str(n) for n in range(1, 5)], 3)
print(len(ps))
print(len(cs))