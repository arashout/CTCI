from problems.utils.testing import Solution, Test

def is_unique_chars(string: str) -> bool:
    if len(string) > 128:
        return False

    seen_table = [False] * 128

    for l in string:
        index = ord(l)
        if seen_table[index]:
            return False
        else:
            seen_table[index] = True

    return True

Solution(
    is_unique_chars,
    [ 
        Test(['ab'], True),
        Test(['aba'], False)
    ]
)
