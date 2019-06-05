import pprint
def isMatch(s: str, p: str):
    n = len(s)
    m = len(p)
    T = [[False for _ in range(m+1)] for _ in range(n+1)]
    T[0][0] = True # Corresponds to empty string empty pattern
    
    for j in range(2, m+1, 2):
        if p[j-1] == '*' and T[0][j-2]:
            T[0][j] =  True
    # i, j are T indices
    for i in range(1, n+1):
        for j in range(1, m+1):
            # String Indices
            ii = i - 1
            jj = j - 1
            if s[ii] == p[jj] or p[jj] == '.':
                T[i][j] = T[i-1][j-1]
            elif p[jj] == '*':
                T[i][j] = T[i][j-2]
                if s[ii] == p[jj-1] or p[jj-1] == '.':
                    T[i][j] = T[i][j] or T[i-1][j]
    for row in T:
        pprint.pprint(row)
    
    return T[len(s)][len(p)]


# isMatch("abaa", "ab..")
isMatch("abaa", ".*")