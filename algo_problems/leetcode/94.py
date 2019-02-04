from typing import NamedTuple, List


class Node(NamedTuple):
    val: int
    left: 'Node'
    right: 'Node'


tree0 = None  # empty tree
tree1 = Node(5, None, None)
tree2 = Node(7, tree1, None)
tree3 = Node(7, tree1, Node(9, None, None))
tree4 = Node(2, None, tree3)
tree5 = Node(2, Node(1, None, None), tree3)
tree6 = Node(-1, tree5, Node(10, None, None))


def check_flattener(f):
    assert f(tree0) == []
    assert f(tree1) == [5]
    assert f(tree2) == [5, 7]
    assert f(tree3) == [5, 7, 9]
    assert f(tree4) == [2, 5, 7, 9]
    assert f(tree5) == [1, 2, 5, 7, 9]


def flatten(bst):
    # empty case
    if bst is None:
        return []
    # node case
    return flatten(bst.left) + [bst.val] + flatten(bst.right)


def flatten2(root: Node) -> List[int]:
    if root is None:
        return []

    cs = []
    res = []
    
    while True:
        if root is not None:
            res.append(root.val)
            cs.append(root)
            root = root.left
        else:
            if len(cs) == 0:
                return res
            else:
                root = cs.pop()
                root = root.right
    return res


def descendLeft(n: Node, acc: []):
    while n is not None:
        acc.append(n)
        n = n.left


print(flatten2(tree6))