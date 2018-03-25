from algo_problems.utils.testing import Solution, Test
from algo_problems.utils.graph import UndirectedGraph, build_simple_graph
from algo_problems.utils.queue import Queue

from typing import Dict


def has_path(g: UndirectedGraph, v: int, w: int) -> bool:
    def helper(_v: int, _w: int, seen: Dict[int, bool]):
        if _v == _w:
            return True

        seen[_v] = True
        for u in g.adj(_v):
            if u in seen:
                pass
            elif helper(u, _w, seen):
                return True
        return False
    
    return helper(v, w, {})
    

def has_path2(g: UndirectedGraph, v: int, w:int) -> bool:
    q = Queue()
    seen: Dict[i, bool] = {}

    q.enqueue(v)
    while not q.is_empty():
        u = q.dequeue()

        if u in seen:
            pass
        else:
            if u == w:
                return True
            for vertex in g.adj(u):
                q.enqueue(vertex)
    
    return False
    
g1 = build_simple_graph(7,
                        [
                            (1, 2),
                            (2, 6),
                            (2, 5),
                            (4, 5),
                            (3, 1),
                            (3, 6)
                        ]
                        )
Solution(
    has_path,
    [
        Test(
            [g1, 1, 3],
            False,
            None
        ),
        Test(
            [g1, 3, 5],
            True,
            None
        )
    ]
)

Solution(
    has_path2,
    [
        Test(
            [g1, 1, 3],
            False,
            None
        ),
        Test(
            [g1, 3, 5],
            True,
            None
        )
    ]

)