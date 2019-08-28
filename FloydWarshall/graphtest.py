# File: graphtest.py

"""
This module implements a general test suite for graphs that extends
the generic consoletest module.  The GraphConsoleTest class implements
only the framework common to all graph algorithms.  Clients that want
to test specific implementations extend this framework with a new
subclass that adds any new commands required for that implementation.
"""

from consoletest import ConsoleTest
from graph import Graph, Node, Arc
from graphtools import readGraphData
from tokenscanner import TokenScanner

class GraphConsoleTest(ConsoleTest):

    def __init__(self):
        self.graph = Graph()
        self.run()

# Commands

    def clearCommand(self, scanner):
        """clear -- Clears the graph"""
        self.graph.clear()

    def loadCommand(self, scanner):
        """load filename -- Loads the graph data from the file"""
        filename = scanner.nextToken()
        ttype = scanner.getTokenType(filename)
        if ttype == TokenScanner.WORD:
            filename += ".txt"
        elif ttype == TokenScanner.STRING:
            filename = scanner.getStringValue(filename)
        else:
            print("Illegal file name")
        readGraphData(self.graph, filename)

    def nodeCommand(self, scanner):
        """node name -- Inserts a node with the specified name"""
        self.graph.addNode(self.scanNodeName(scanner))

    def arcCommand(self, scanner):
        """arc n1 n2 [cost] -- Adds an arc from n1 to n2"""
        n1 = self.scanNodeName(scanner)
        if self.graph.findNode(n1) is None:
            n1 = self.graph.addNode(n1)
        n2 = self.scanNodeName(scanner)
        if self.graph.findNode(n2) is None:
            n2 = self.graph.addNode(n2)
        cost = 0
        if scanner.hasMoreTokens():
            cost = self.scanNumber()
        arc = self.graph.addArc(n1, n2)
        arc.setCost(cost)

    def arcsCommand(self, scanner):
        """arcs -- Lists the arcs in the graph"""
        for arc in self.graph.getArcs():
            start = arc.getStart()
            finish = arc.getFinish()
            arcstr = str(arc)
            if self.isBidirectional(arc):
                if start < finish:
                    arcstr = arcstr.replace(" -> ", " - ")
                    print(arcstr)
            else:
                print(arcstr)

    def arcsFromCommand(self, scanner):
        """arcsFrom node -- Lists the arcs that start at node"""
        for arc in self.scanNode(scanner).getArcsFrom():
            start = arc.getStart()
            finish = arc.getFinish()
            arcstr = str(arc)
            if self.isBidirectional(arc):
                arcstr = arcstr.replace(" -> ", " - ")
            print(arcstr)

    def arcsToCommand(self, scanner):
        """arcsTo node -- Lists the arcs that end at node"""
        for arc in self.scanNode(scanner).getArcsTo():
            start = arc.getStart()
            finish = arc.getFinish()
            arcstr = str(arc)
            if self.isBidirectional(arc):
                arcstr = arcstr.replace(" -> ", " - ")
            print(arcstr)

    def nodesCommand(self, scanner):
        """nodes -- Lists the nodes in the graph"""
        for node in self.graph.getNodes():
            print(node)

    def neighborsCommand(self, scanner):
        """neighbors node -- Lists the nodes to which node connects"""
        for arc in self.scanNode(scanner).getArcs():
            print(arc.getFinish())

# Methods used by subclasses

    def getGraph(self):
        """Returns the graph used in this test package."""
        return self.graph

    def scanNumber(self, scanner):
        """Reads a number from the scanner, which may include a sign."""
        sign = 1
        token = scanner.nextToken()
        if token == "-":
            sign = -1
            token = scanner.nextToken()
        return sign * float(token)

    def scanNodeName(self, scanner):
        """Reads the name of a node from the scanner."""
        token = scanner.nextToken()
        ttype = scanner.getTokenType(token)
        if ttype == TokenScanner.EOF:
            raise SyntaxError("Missing node name")
        elif ttype == TokenScanner.WORD or ttype == TokenScanner.NUMBER:
            return token
        elif ttype == TokenScanner.STRING:
            return scanner.getStringValue(token)
        else:
            raise SyntaxError("Illegal node name: " + name)

    def scanNode(self, scanner):
        """Reads the next token and makes sure it is a node name."""
        name = self.scanNodeName(scanner)
        node = self.graph.findNode(name)
        if node is None:
            raise SyntaxError("Undefined node: " + name)
        return node

    def isBidirectional(self, arc):
        """Returns True if the arc is bidirectional."""
        for incoming in arc.getStart().getArcsTo():
            if incoming.getStart() == arc.getFinish():
                if incoming.getCost() == arc.getCost():
                    return True
        return False

# Startup code

if __name__ == "__main__":
    GraphConsoleTest()
