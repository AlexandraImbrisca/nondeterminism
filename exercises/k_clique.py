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
    success()
