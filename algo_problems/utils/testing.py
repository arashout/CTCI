from typing import Callable, NamedTuple, Any, List, Dict

def assert_with_messages(i: int, args: List[Any], actual: Any, expected: Any, success_msg = '.'):
    def success_helper(line_ending = '') -> bool:
        print(success_msg, end=line_ending, flush=True)
        return True

    failed_message = """
    Failed on test number {0}. With arguments:
    {1}
    Actual:
    {2}
    Expected:
    {3}
    """.format(i+1, args, actual, expected)
    assert actual == expected and success_helper(), failed_message

# TODO: Add post processing function call
class Test(NamedTuple):
    """ Test data class to be used in conjunction with a Solution class
    
    Arguments:
        args: List[Any]
        expected: Any
        mutated: Any
    """

    args: List[Any]
    expected: Any
    mutated: Any
    
class Solution:
    def __init__(self, function: Callable, test_table: List[Test], name = '', stub = ''):

        # Run tests from test table
        for i, t in enumerate(test_table):
            if t.mutated is None:
                actual = function(*t.args)
                assert_with_messages(i, t.args, actual, t.expected)
            else:
                function(*t.args)
                assert_with_messages(i, t.args, t.mutated, t.expected)
        
        print('\n{0} Tests passed'.format(len(test_table)))
    
# TODO: Create class called Command so I can determine how many args are needed
class Command(NamedTuple):
    func: Callable
    num_args: int
    name: str

def command_test_loop(commands_mapping: Dict[str, Command], default_call: Callable):
    for c_string, c in commands_mapping.items():
        print('{0} -> {1}'.format(c_string,c.name))
        
    while True:
        c_string = input()
        command = commands_mapping.get(c_string, None)
        if command is None:
            default_call()
        else:
            if command.num_args == 0:
                command.func()
            else:
                args = input('Arg for {0}:\n'.format(command.name))
                try:
                    args = eval(args)
                    command.func(args)
                except ValueError:
                    command.func('')
        