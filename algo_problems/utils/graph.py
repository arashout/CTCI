from typing import List, Any

class Node:
    def __init__(self, val:Any, connections: List[Node] = []):
        self.val = val
        self.connections = connections
    