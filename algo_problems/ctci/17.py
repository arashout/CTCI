from typing import List
from algo_problems.utils.testing import Test, Solution


def rotate(m: List[List[int]]) -> List[List[int]]:
    n = len(m)
    for layer in range( int(n / 2)):
        first = layer
        last = n - (1 + layer)

        for i in range(first, last):
            offset = i - first
            top = m[first][i]
            m[first][i] = m[last - offset][first]  # Left -> Top
            m[last - offset][first] = m[last][last - offset]  # Bottom -> Left
            m[last][last - offset] = m[i][last]  # Right -> Bottom
            m[i][last] = top  # Top -> Right

    return m

Solution(
    rotate,
    [
        Test(
            [
                [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]
                ]
            ],
            [
                [7, 4, 1],
                [8, 5, 2],
                [9, 6 ,3],
            ]
        )
    ]
)
