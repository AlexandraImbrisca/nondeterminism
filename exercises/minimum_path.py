from nondeterminism import *
from helpers import Graph


@nondeterministic
def minimum_path(g: Graph, u: int, v: int, dim: int):
    """
    Are two vertices connected through a path with the maximum size dim?

    :param g: The graph.
    :param u: The initial vertex.
    :param v: The final vertex.
    :param dim: The maximum number of edges included in the path (including
    the initial & final nodes).
    :return: True if there's such a path. False otherwise
    """

    if g.has_edge(u, v) and dim >= 1:
        success()

    path = []
    while True:
        i = choice(g.vertices)
        if i in path:
            fail()
        path.append(i)

        if len(path) + 2 >= dim:
            fail()

        for idx in range(len(path) - 1):
            if not g.has_edge(path[idx], path[idx + 1]):
                fail()

        if g.has_edge(u, path[0]) and g.has_edge(path[len(path) - 1], v):
            success()
