from algo_problems.utils.testing import Solution, Test
from typing import List


def urlify(char_list: List[str],  true_length: int) -> List[str]:
    count_all_spaces = 0
    for c in char_list:
        if c == ' ':
            count_all_spaces += 1

    # Space is normally 1 character while %20 is 3
    # 2 additional characters per space
    count_spaces = count_all_spaces // 3
    offset = count_spaces * 2
    # Reverse for loop to take advantage of buffer at end
    # and not overwriting anything when moving
    for i in range((true_length - 1) - offset, 0, -1):
        c = char_list[i]
        if c != ' ':
            char_list[i + offset] = c
        else:
            char_list[i + offset] = '0'
            char_list[i + offset - 1] = '2'
            char_list[i + offset - 2] = '%'
            # For the buffer we have 'lost'
            offset -= 2
            if offset == 0:
                return char_list
    
    # For testing
    return char_list

Solution(
    urlify,
    [
        Test([list('Mr John Smith    '), 17], list('Mr%20John%20Smith')),
    ]
)