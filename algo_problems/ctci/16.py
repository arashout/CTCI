from problems.utils.testing import Solution, Test
from Testing import Solution, Test

def compress_string(s: str) -> str:
    new_s = ''
    i = 0

    while True:
        count = 1
        j = i + 1
        while j < len(s):
            if s[i] == s[j]:
                count += 1
                j += 1
            else:
                new_s += s[i] + str(count)
                i = j
                break

        if j >= len(s):
            if j > len(s):
                return s
            
            new_s += s[i] + str(count)
            break
    
    if len(new_s) >= len(s):
        return s

    return new_s

Solution(
    compress_string,
    [
        Test(['aaabb'], 'a3b2'),
        Test(['aaabbba'], 'a3b3a1'),
        Test(['a'], 'a'),
        Test([''], ''),
        Test(['aba'], 'aba'),
        Test(['aaaaa'], 'a5'),
    ]
)
