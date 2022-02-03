from nondeterminism import *
from helpers import Graph


@nondeterministic
def independent_set(g: Graph, k: int):
    """
    Is there a subset S of k vertices such that each edge from g has at most
    one vertex in S?

    :param g: The graph.
    :param k: The desired number of vertices
    :return: True if the condition is satisfied, false otherwise.
    """
    S = []
    for i in range(k):
        u = choice(g.vertices)
        if u in S:
            fail()
        S.append(u)

    for (u, v) in g.edges:
        if u in S and v in S:
            fail()
    success()
