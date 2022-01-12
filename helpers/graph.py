class Graph:
    def __init__(self, vertices: list, edges: list):
        self.vertices = vertices
        self.edges = edges

    def has_edge(self, u: int, v: int) -> bool:
        # Undirected graph
        return (u, v) in self.edges or (v, u) in self.edges
