# File: FloydWarshall.py

"""
This module implements the Floyd-Warshall algorithm for solving the
all-pairs shortest-path problem.
"""

import math

# Implementation notes
# --------------------
# The Floyd-Warshall algorithm operates by computing successive
# distance matrices d[i][j] in which each element contains the
# shortest distance from node i to node j, considering only paths
# that pass through a set of points that grows on each cycle.
# On cycle k (where k runs from 0 to n - 1), the distance includes
# paths that pass through nodes with indices up to k.

def computeFloydWarshallMatrices(g):
    """
    Returns a tuple of the distance and predecessor matrices
    computed by the Floyd-Warshall algorithm when applied to g.
    """
    n = len(g)
    d = createInitialDistanceMatrix(g)
    p = createInitialPredecessorMatrix(g)
    for k in range(n):
        d2 = copyMatrix(d)
        p2 = copyMatrix(p)
        for i in range(n):
            for j in range(n):
                newDistance = d[i][k] + d[k][j]
                if newDistance < d[i][j]:
                    d2[i][j] = newDistance
                    p2[i][j] = p[k][j]
        d = d2
        p = p2
    return (d,p)

def createInitialDistanceMatrix(g):
    """
    Returns the initial distance matrix d, which is constructed
    from the nodes and arcs in the graph g.  Element d[i][j] is 0
    if i == j, the length of the shortest arc in g that connects
    nodes i and j, and infinity if no connecting arc exists.
    """
    nodes = g.getNodes();
    n = len(nodes)
    d = [ [ math.inf ] * n for i in range(n) ]
    for i in range(n):
        for j in range(n):
            if i == j:
                d[i][j] = 0
            else:
                d[i][j] = minimumArcCost(nodes[i], nodes[j])
    return d

def createInitialPredecessorMatrix(g):
    """
    Returns the initial predecessor matrix p, which is constructed
    from the nodes and arcs in the graph g.  Element p[i][j] is i
    if there is an arc from i to j, and None if no connecting arc
    exists.
    """
    nodes = g.getNodes();
    n = len(nodes)
    p = [ [ None ] * n for i in range(n) ]
    for i in range(n):
        for j in range(n):
            if i != j and nodes[i].isConnectedTo(nodes[j]):
                p[i][j] = i
    return p

def copyMatrix(m):
    """Returns a copy of matrix m, which must be square."""
    n = len(m)
    return [ [ m[i][j] for j in range(n) ] for i in range(n) ]

def minimumArcCost(n1, n2):
    """Returns the minimal cost of the arcs between n1 and n2."""
    minCost = math.inf
    for arc in n1.getArcs():
        if arc.getFinish() == n2:
            minCost = min(minCost, arc.getCost())
    return minCost
