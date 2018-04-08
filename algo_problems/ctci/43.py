from algo_problems.utils.tree import BinaryTreeNode, parse_tree
from algo_problems.utils.linked_list import SinglyLinkedList
from queue import Queue
from typing import List, NamedTuple

class QueueNode(NamedTuple):
    bt_node: BinaryTreeNode
    depth: int

def list_of_depths(root: BinaryTreeNode) -> SinglyLinkedList:
    if root is None:
        return None

    q = Queue()
    q.put(QueueNode(root, 0))

    ll_container: List[SinglyLinkedList] = [SinglyLinkedList()]

    current_depth = 0

    while not q.empty():
        q_node: QueueNode = q.get()
        
        if current_depth < q_node.depth:
            ll_container.append(SinglyLinkedList())
            current_depth = q_node.depth

        # Check if any nodes at this depth have been added
        ll = ll_container[-1]
        ll.prepend(q_node.bt_node)

        # Add children to queue with depth information
        if q_node.bt_node.left is not None:
            q.put(QueueNode(q_node.bt_node.left, q_node.depth + 1))
        if q_node.bt_node.right is not None:
            q.put(QueueNode(q_node.bt_node.right, q_node.depth + 1))

    return ll_container


def print_list_of_depths(list_of_depths: List[SinglyLinkedList]):

    for depth, ll in enumerate(list_of_depths):
        print('\n{0}:'.format(depth), end='\t')

        for item in ll:
            print(item, end=' ')
    
    print()

if __name__ == '__main__':
    # print_list_of_depths(list_of_depths(parse_tree('1(2,3)')))
    print_list_of_depths(list_of_depths(parse_tree('1(2(10,),3(4,5(6,7)))')))