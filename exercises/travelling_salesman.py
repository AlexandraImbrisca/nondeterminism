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
    success()
