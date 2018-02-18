from typing import List
from algo_problems.utils.testing import Test, Solution


def zero_matrix(mat: List[List[int]]) -> List[List[int]]:
    n = len(mat)
    m = len(mat[0])

    r = {}
    c = {}

    for i in range(0, n):
        for j in range(0, m):
            if(i in r):
                break

            if mat[i][j] == 0:
                r[i] = True
                c[j] = True

    # Zero rows
    for i in r.keys():
        for j in range(0, m):
            mat[i][j] = 0

    # Zero cols
    for j in c.keys():
        for i in range(0, n):
            mat[i][j] = 0

    return mat


Solution(
    zero_matrix,
    [
        Test(
            [
                [
                    [1, 2, 3],
                    [1, 2, 0]
                ]

            ],
            [
                [1, 2, 0],
                [0, 0, 0]
            ]
        ),
        Test(
            [
                [
                    [0, 2, 3],
                    [1, 2, 0]
                ]

            ],
            [
                [0, 0, 0],
                [0, 0, 0]
            ]
        )
    ]
)
