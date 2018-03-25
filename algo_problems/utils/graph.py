from typing import List, Tuple

class UndirectedGraph:
    def __init__(self, n: int):
        self.vertices: List[list] = [[] for i in range(n)]
    
    def add_edge(self, i: int, j:int, undirected = False):
        # Check if within bounds
        if i >= len(self.vertices) or j >= len(self.vertices):
            # TODO: Add more information?
            raise IndexError('Vertex index out of bounds')

        self.vertices[i].append(j)
        
        if undirected:
            self.vertices[j].append(i)
    
    def adj(self, i: int):
        return self.vertices[i]


def build_simple_graph(n: int, edges: tuple) -> UndirectedGraph:
    g = UndirectedGraph(n)
    for e in edges:
        g.add_edge(e[0], e[1])
    return g

    