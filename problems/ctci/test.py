from Testing import Solution, Test

def func(arg1, arg2):
    return arg1 + str(arg2)

test_table = [
    Test(
        args = ['1', True],
        expected = '1True'
    ),
    Test(['2', True],'2True')
]

Solution(
    func,
    test_table,
    '11'
    'func(arg1, arg2)'
)

