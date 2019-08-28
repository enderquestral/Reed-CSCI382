# File: dijkstra.py

"""
This module implements Dijkstra's algorithm for solving the single-source
shortest-path problem.
"""

#Got help from Jonah Kohn (regarding making frontier iteratable)
#Worked a bit with Casey Harris and Jirarong Li
# -Hannah

from pqueue import PriorityQueue
import math

# Implementation notes
# --------------------
# This implementation of Dijkstra's algorithm follows the logic of the
# pseudocode from CLRS and computes the minimum distance from the start
# node to every other node in the graph.  Unlike Dijkstra's original
# algorithm, it does not support stopping when a destination node is
# reached or visiting only a subset of the nodes.  It also uses an
# implementation of the PriorityQueue class that does not guarantee
# the logarithmic time performance of the raisePriority method.  Your
# job on the assignment is to repair these deficiencies.

def applyDijkstraOrig(g, start):
    """
    Applies Dijkstra's algorithm to the graph g, updating the
    distance from start to each node in g.
    """
    initializeSingleSource(g, start)
    finalized = set()
    pq = PriorityQueue()
    for node in g.getNodes():
        pq.enqueue(node, node.distance)
    while not pq.isEmpty():
        node = pq.dequeue()
        finalized.add(node)
        for arc in node.getArcsFrom():
            n1 = arc.getStart()
            n2 = arc.getFinish()
            if n2 not in finalized:
                oldDistance = n2.distance
                relax(n1, n2, arc.getCost())
                if n2.distance < oldDistance:
                    pq.raisePriorityOrig(n2, n2.distance)


def applyDijkstra(g, start, finish):
    """
    Applies Dijkstra's algorithm to the graph g, updating the
    distance from start to each node in g.
    """
    #MAKE SURE THAT THE ALGORITHM IS APPLIED ONLY TO THE START/FINISH NODE
    #USE node.predecessor, node.distance
    
    #initializeSingleSource(g, start)

    finalized = set()
    frontier = PriorityQueue()
    finishedendnode = False
    #explored = set()
    start.distance = 0
    start.predecessor = None

    frontier.enqueue(start)

    while not frontier.isEmpty() and finishedendnode == False:
        node = frontier.dequeue()
        #print(type(node))
        finalized.add(node)
        if node == finish:
            finishedendnode = True
            break
        for arc in node.getArcsFrom():
            n1 = arc.getStart()
            n2 = arc.getFinish()
            #print("n1: "+ str(n1))
            #print("n2: "+ str(n2))
            #print("node: "+ str(node))
            if n2 not in finalized:
                #print("n2: "+ str(n2))
                if n2 not in frontier:
                    initIndivNode(n1, n2, arc)
                    frontier.enqueue(n2, n2.distance)
                #init single source
                else:
                    oldDistance = n2.distance
                    relax(n1, n2, arc.getCost())
                    if n2.distance < oldDistance:
                        frontier.raisePriority(n2, n2.distance)



def initIndivNode(n1,n2,arc):
    n2.distance = n1.distance + arc.getCost()
    n2.predecessor = n1


def initializeSingleSource(g, start):
    """Initialize the distance and predecessor attributes."""
    for node in g.getNodes():
        node.distance = math.inf
        node.predecessor = None
    start.distance = 0

def relax(n1, n2, cost):
    """Update the fields of n2 using the path n1 -> n2."""
    if n2.distance > n1.distance + cost:
        n2.distance = n1.distance + cost
        n2.predecessor = n1
