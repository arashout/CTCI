from algo_problems.utils.testing import Solution, Test
from algo_problems.utils.graph import Graph, Vertex, build_simple_graph

from typing import Dict


def has_path(v: Vertex, w: Vertex) -> bool:
    def helper(_v: Vertex, _w: Vertex, seen: Dict[Vertex, bool]):
        if _v == _w:
            return True

        seen[_v] = True
        for u in _v.children:
            if u in seen:
                pass
            elif helper(u, _w, seen):
                return True
        return False
    
    return helper(v, w, {})
    

def has_path2(v: Vertex, w:Vertex) -> bool:
    # TODO: Implement with breadth first search
    raise NotImplementedError

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
            [g1.get_vertex_by_index(1), g1.get_vertex_by_index(3)],
            False,
            None
        ),
        Test(
            [g1.get_vertex_by_index(3), g1.get_vertex_by_index(5)],
            True,
            None
        )
    ]
)

Solution(
    has_path2,
    [
        Test(
            [g1.get_vertex_by_index(1), g1.get_vertex_by_index(3)],
            False,
            None
        ),
        Test(
            [g1.get_vertex_by_index(3), g1.get_vertex_by_index(5)],
            True,
            None
        )
    ]

)