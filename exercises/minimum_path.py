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
    success()
