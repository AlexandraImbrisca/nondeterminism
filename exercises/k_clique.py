from nondeterminism import *
from helpers import Graph


@nondeterministic
def k_clique(g: Graph, k: int):
    """
    Is there a complete subgraph of k vertices?
    (complete = all nodes are connected to each other).

    :param g: The graph.
    :param k: The desired size.
    :return: False if no graph of size k is complete. True otherwise.
    """

    selected_vertices = []
    for i in range(k):
        u = choice(g.vertices)
        if u in selected_vertices:
            fail()
        selected_vertices.append(u)

    for u in selected_vertices:
        for v in selected_vertices:
            if u != v and not g.has_edge(u, v):
                fail()

    success()
