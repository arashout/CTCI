from Testing import Solution, Test

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


assert s.solution(is_unique_chars, 'ab') == True
assert s.solution(is_unique_chars, 'aba') == False