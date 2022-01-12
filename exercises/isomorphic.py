from nondeterminism import *
from helpers import Graph


@nondeterministic
def isomorphic(g1: Graph, g2: Graph):
    """
    Is there a function f that for each vertex v1 from g1 associates a vertex
    v2 from g2 such that the edges also correspond?
    (If g1 contains the edge (u, v) then g2 must contain the edge (f(u), f(v)).

    NOTE: the property is a bidirectional property. If g2 contains (f(u), f(v))
    then g1 must contain (u, v) (=> g1, g2 must have the same number of vertices
    and edges)

    :param g1: The first graph.
    :param g2: The second graph.
    :return: True if there is at least one function that satisfies the
    condition. Otherwise, it returns false.
    """
    success()
