from nondeterminism import *
from helpers import Graph


@nondeterministic
def vertex_cover(g: Graph, k: int):
    """
    Is there a subset S of k vertices such that each edge from g has at least
    one vertex in S?

    :param g: The graph.
    :param k: The desired number of vertices
    :return: True if the condition is satisfied, false otherwise.
    """
    success()
