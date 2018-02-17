from problems.utils.testing import Solution, Test
from typing import List

def is_permutation_of_palindrome(char_list: List[str]) -> bool:
    freq_table = {}

    for c in char_list:
        if c in freq_table:
            freq_table[c] += 1
        else:
            freq_table[c] = 1
    
    count_odd = 0
    for count in freq_table.values():
        if count % 2 != 0 :
            count_odd += 1
            if count_odd > 1:
                return False
    
    return True

# Improved solution with bit vector
def is_permutation_of_palindrome_optimized(char_list: List[str]) -> bool:
    def toggle_bit(vector, k) -> int:
        mask = 1 << k
        return vector ^ mask
    
    # Python 32 bit integer so assuming only lowercase alphabet
    bit_vector = 0
    
    offset = ord('a')
    for c in char_list:
        value = ord(c) - offset
        bit_vector = toggle_bit(bit_vector, value)
    
    # If bit_vector is power of two, it means there's only on odd toggle
    # e.g. 00100 - 00001 = 00011 <- Notice that the 'and' of bit_vector & result is 0
    odd_mask = bit_vector - 1
    is_power_of_two = not (bit_vector & odd_mask)
    return bit_vector == 0 or is_power_of_two

Solution(
    is_permutation_of_palindrome,
    [
        Test([list('yaya')], True),
        Test([list('yayaa')], True),
        Test([list('baabcccddd')], False),
        Test([list('')], True),
    ]
)

Solution(
    is_permutation_of_palindrome_optimized,
    [
        Test([list('yaya')], True),
        Test([list('yayaa')], True),
        Test([list('baabcccddd')], False),
        Test([list('')], True),
    ]
)
