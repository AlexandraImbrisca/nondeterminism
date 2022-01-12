from nondeterminism import *
from helpers import Graph


@nondeterministic
def k_color(g: Graph, k: int):
    """
    Can we associate a color to each node of the graph such that no adjacent
    nodes have the same color? We can use at most k colors.

    :param g: The graph.
    :param k: The maximum number of colors.
    :return: True if possible, false otherwise.
    """
    success()
