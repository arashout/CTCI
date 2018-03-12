from typing import List, Any, Tuple

class Vertex:
    children: List['Vertex']
    
    def __init__(self, val:Any):
        self.val = val
        self.children = []
    
    def __repr__(self) -> str:
        return  'v: {0}'.format(self.val)
class Graph:
    def __init__(self, vertices: List[Vertex] = []):
        self.vertices = vertices
    
    def get_vertex_by_index(self, i: int) -> Vertex:
        if i >= len(self.vertices):
            # TODO: Add more information?
            raise IndexError('Vertex index out of bounds')
        return self.vertices[i]
    
    def add_vertex(self, v: Vertex):
        self.vertices.append(v)
    
    def add_edge_by_index(self, i: int, j: int, undirected = False):
        # Check if within bounds
        if i >= len(self.vertices) or j >= len(self.vertices):
            # TODO: Add more information?
            raise IndexError('Vertex index out of bounds')

        v = self.vertices[i]
        w = self.vertices[j]
        v.children.append(w)

        if undirected:
            w.children.append(v)



def build_simple_graph(n: int, edges: tuple) -> Graph:
    g = Graph([Vertex(i) for i in range(n)])
    for e in edges:
        g.add_edge_by_index(e[0], e[1])
    return g

    