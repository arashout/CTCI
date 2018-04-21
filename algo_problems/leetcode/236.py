from algo_problems.utils.tree import parse_tree

class Result:
    def __init__(self, node, isAncestor):
        self.node = node
        self.isAncestor = isAncestor
        
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def helper(node, p, q):
            if node is None:
                return Result(None, False)
            elif node == p and node == q:
                return Result(node, True)

            
            rx = helper(node.left, p, q)
            if rx.isAncestor:
                return rx

            ry = helper(node.right, p, q)
            if ry.isAncestor:
                return ry
            
            if rx.node is not None and ry.node is not None:
                return Result(node, True)
            elif node == p or node == q:
                isAncestor = rx.node is not None or ry.node is not None
                return Result(node, isAncestor)
            else:
                nodeToReturn = rx.node if rx.node is not None else ry.node
                return Result(nodeToReturn, False)
        
        r = helper(root, p, q)
        return r.node
    
t = parse_tree('3(5(6,2(7,4)),1(0,8))')
p = t.left
q = t.left.right.right
print(t)
s = Solution()
r = s.lowestCommonAncestor(t, p,q)
print(r)