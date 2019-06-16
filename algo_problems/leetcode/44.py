def isMatch( s: str, p: str) -> bool:
    n = len(s)
    m = len(p)
    def helper(i: str, j: str) -> bool:
        a = s[i] if i < n else ''
        b = p[j] if j < m else ''
        if a == '' and b == '':
            return True
        # If only one of them is an empty string
        elif a == '' and b not in {'', '*'}:
            return False
        # Consume from both string and pattern
        elif a == b or b == '?':
            return helper(i+1, j+1)
        elif i <= n and b == '*':
            return helper(i+1, j+1) or helper(i+1, j) or helper(i,j+1)
        else:
            return False
    return helper(0,0)

def isMatchFSM(s:str, p:str) -> bool:
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    transfer = {}
    state = 0
    
    for char in p:
        if char == '*':
            transfer[state, char] = state
        else:
            transfer[state, char] = state + 1
            state += 1
    
    accept = state
    state = set([0])
    
    for char in s:
        nextState = set()
        # NOTE: Because * and ? can match any character, they can always be used to access the next state
        # Notice that transfer.get will only be successful with * and ? when there exists an entry inside the transfer dict
        # as dictated by the regex string p!
        for token in [char, '*', '?']:
            for at in state:
                nextState.add(transfer.get((at, token)))
        state = nextState
    
    return accept in state

print(isMatchFSM("adceb", "a*b"))
print(isMatchFSM("adceb", "*a*b"))
print(isMatchFSM("acdcb", "a*c?b"))
print(isMatchFSM("ab", "?*"))
print(isMatchFSM("", "*"))
print(isMatchFSM("", "**"))