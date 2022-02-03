from nondeterminism import *
from helpers import Graph


@nondeterministic
def travelling_salesman(g: Graph):
    """
    Can a travelling salesman visit every city exactly once and return to the
    starting point?

    :param g: The graph containing the cities and the connections between them.
    :return: False if there is no valid path. True otherwise.
    """
    path = []
    for i in range(len(g.vertices)):
        u = choice(g.vertices)
        if u in path:
            fail()
        path.append(u)

    for idx in range(len(path) - 1):
        if not g.has_edge(path[idx], path[idx + 1]):
            fail()

    if not g.has_edge(path[len(path) - 1], path[0]):
        fail()
    success()
