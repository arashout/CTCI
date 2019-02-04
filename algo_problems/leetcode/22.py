# TODO: Implement this in Rust to figure out how to join vectors
# 1. BackTracking Solution
# class Solution(object):
#     def generateParenthesis(self, n):
#         """
#         :type n: int
#         :rtype: List[str]
#         """
#         def helper(chars, left, right, n):
#             if len(chars) == 2*n:
#                 return [''.join(chars)]
                        
#             if left < n and right < left:
#                 return helper(chars + ['('], left + 1, right, n) + helper(chars + [')'], left, right+1, n)
#             elif left < n:
#                 return helper(chars + ['('], left + 1, right, n)
#             elif right < left:
#                 return helper(chars + [')'], left, right+1, n)
#             else:
#                 return []
        
#         return helper([], 0, 0, n)