from Testing import Solution, Test
from typing import List

def one_away(a: str, b: str) -> bool:
    n_a = len(a)
    n_b = len(b)

    def n_replacements_away(n: int) -> bool:
        count_replacements = 0
        for i in range(n_a):
            if a[i] != b[i]:
                count_replacements += 1
            
            if count_replacements > n:
                return False
        return True
    
    def one_insertion_away(shorter: str, longer: str) -> bool:
        offset = 0
        one_error_found = False
        for i in range(len(shorter)):
            if shorter[i] != longer[i+offset]:
                offset += 1

                if one_error_found:
                    return False

                one_error_found = True
        return True

    if n_a == n_b:
        return n_replacements_away(1)
    elif (n_a - n_b) == 1:
        return one_insertion_away(b, a)
    elif (n_b - n_a) == 1:
        return one_insertion_away(a, b)
    else:
        return False

Solution(
    one_away,
    [
        Test(['pale', 'ple'], True),
        Test(['pale', 'pale'], True),
        Test(['pale', 'pales'], True),
        Test(['pale', 'pl'], False),
        Test(['pale', 'bale'], True),
        Test(['pale', 'bals'], False),
        Test(['a', ''], True)
    ]
)
