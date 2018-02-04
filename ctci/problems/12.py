from Testing import Solution, Test

def check_permutation(a: str, b: str) -> bool:
    freq_table = [0] * 128
    if len(a) != len(b):
        return False

    for l in a:
        val = ord(l)
        freq_table[val] += 1
    
    for l in b:
        val = ord(l)
        freq_table[val] -= 1
        if freq_table[val] == -1:
            return False
    
    return True

Solution(
    check_permutation,
    [
        Test(['aba','ab'], False),
        Test(['same', 'mase'], True),
        Test(['diff','diph'], False)
    ]
)