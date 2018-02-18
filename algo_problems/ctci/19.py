from algo_problems.utils.testing import Test, Solution

def is_rotation(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    xyxy = s1 + s1

    return (s2 in xyxy)

Solution(
    is_rotation,
    [
        Test(
            ['waterbottle', 'erbottlewat'],
            True
        ),
        Test(
            ['waterbottles', 'ewatserbottle'],
            False
        )
    ]
)