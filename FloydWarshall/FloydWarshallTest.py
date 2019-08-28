# File: FloydWarshallTest.py

"""
This module extends the GraphConsoleTest module to test the
Floyd-Warshall algorithm.
"""

from graphtest import GraphConsoleTest
from FloydWarshall import computeFloydWarshallMatrices

# Constants

COLUMN_WIDTH = 5

# Test program

class FloydWarshallTest(GraphConsoleTest):

    def __init__(self):
        GraphConsoleTest.__init__(self)

    def distancesCommand(self, scanner):
        """distances -- Prints the shortest-distance matrix for the graph"""
        d,p = computeFloydWarshallMatrices(self.graph)
        printDistanceMatrix(self.graph.getNodes(), d)

    def predecessorsCommand(self, scanner):
        """predecessors -- Prints the predecessor matrix for the graph"""
        d,p = computeFloydWarshallMatrices(self.graph)
        printPredecessorMatrix(self.graph.getNodes(), p)

    def pathCommand(self, scanner):
        """path start finish -- Compute shortest path from start to finish """
        #Takes names of two nodes, displays the minimum path btwn those nodes
        #The difference is that the data for computing the shortest path
        #comes from the predecessor matrix returned by computeFloydWarshallMatrices function

        start = self.scanNode(scanner)
        finish = self.scanNode(scanner)
        #Get distance and predecessor matrices d and p 
        d,p = computeFloydWarshallMatrices(self.graph)
        #ELEM p[i][j] is 1 if there is an arc fom i to j
        if start == finish:
            print(str(start.getName() + "(0)"))
            return

        #WE NEED INDICES
        holddict  = {}
        holdnodes = self.graph.getNodes()
        for n in range(len(holdnodes)):
            holddict[holdnodes[n]] = n

        nextnode = p[holddict[finish]][holddict[start]] 
        holdpath = []
        holdvalue = d[holddict[finish]][holddict[start]]
        while nextnode != None:
            holdpath.append(holdnodes[nextnode])
            nextnode = p[holddict[finish]][nextnode]
        holdpathstr = start.getName()
        for n in holdpath:
            holdpathstr += (" -> "+ n.getName())

        print("The minimum arc between start and finish is: " + holdpathstr)
        print("The minimum arc cost between start and finish is: (" + str(holdvalue) + ")")

def printDistanceMatrix(nodes, d):
    n = len(nodes)
    header = " " * COLUMN_WIDTH
    for node in nodes:
        header += (node.getName() + " ").rjust(COLUMN_WIDTH)
    print(header.rstrip())
    for i in range(n):
        line = nodes[i].getName().center(COLUMN_WIDTH)
        for j in range(n):
            value = str(d[i][j])
            if value.endswith(".0"):
                value = value[:-2]
            line += (value + " ").rjust(COLUMN_WIDTH)
        print(line.rstrip())

def printPredecessorMatrix(nodes, p):
    n = len(nodes)
    header = " " * COLUMN_WIDTH
    for node in nodes:
        header += node.getName().center(COLUMN_WIDTH)
    print(header.rstrip())
    for i in range(n):
        line = nodes[i].getName().center(COLUMN_WIDTH)
        for j in range(n):
            if p[i][j] is None:
                entry = "-"
            else:
                entry = nodes[p[i][j]].getName()
            line += entry.center(COLUMN_WIDTH)
        print(line.rstrip())
    
# Startup code

if __name__ == "__main__":
    FloydWarshallTest()
