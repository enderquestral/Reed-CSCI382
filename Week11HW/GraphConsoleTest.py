# File: GraphConsoleTest.py

"""
This program implements an interactive test of the graph.py module.
The program starts off with an empty graph and then accepts commands
the user.
"""

from consoletest import ConsoleTest
from graph import Graph, Node, Arc
from graphtools import readGraphData, dfs, bfs
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
            cost = float(scanner.nextToken())
        self.graph.addArc(n1, n2, cost)

    ###    
    # ADDED COMMANDS TO DELETENODE, DELETEARC, AND KAHNS ALGORITHM -HH
    def removeNodeCommand(self, scanner):
        """removeNode name -- Removes a node with the specified name"""
        self.graph.removeNode(self.scanNodeName(scanner))

    def removeArcCommand(self, scanner):
        """removeArc n1 n2 -- Removes the arc from n1 to n2"""
        n1 = self.scanNodeName(scanner)
        n2 = self.scanNodeName(scanner)
        self.graph.removeArc(n1, n2)


    def kahnCommand(self, scanner):
        """kahn -- Calls the topological sort on the graph. Prints it."""
        result = self.graph.KahnsAlgorithm()
        print(result)
    ###
    def arcsCommand(self, scanner):
        """arcs -- Lists the arcs in the graph"""
        for arc in self.graph.getArcs():
            start = arc.getStart()
            finish = arc.getFinish()
            arcstr = str(arc)
            if finish.isConnectedTo(start):
                if start < finish:
                    arcstr = arcstr.replace(" -> ", " - ")
                    print(arcstr)
            else:
                print(arcstr)

    def arcsFromCommand(self, scanner):
        """arcsFrom node -- Lists the arcs that start at node"""
        name = self.scanNodeName(scanner)
        if name is None:
            print("Missing node name")
        else:
            node = self.graph.findNode(name)
            if node is None:
                print("No node named " + name)
            else:
                for arc in node.getArcsFrom():
                    start = arc.getStart()
                    finish = arc.getFinish()
                    arcstr = str(arc)
                    if start.isConnectedTo(finish):
                        arcstr = arcstr.replace(" -> ", " - ")
                    print(arcstr)

    def arcsToCommand(self, scanner):
        """arcsTo node -- Lists the arcs that end at node"""
        name = self.scanNodeName(scanner)
        if name is None:
            print("Missing node name")
        else:
            node = self.graph.findNode(name)
            if node is None:
                print("No node named " + name)
            else:
                for arc in node.getArcsTo():
                    start = arc.getStart()
                    finish = arc.getFinish()
                    arcstr = str(arc)
                    if finish.isConnectedTo(start):
                        arcstr = arcstr.replace(" -> ", " - ")
                    print(arcstr)

    def nodesCommand(self, scanner):
        """nodes -- Lists the nodes in the graph"""
        for node in self.graph.getNodes():
            print(node)

    def neighborsCommand(self, scanner):
        """neighbors node -- Lists the nodes to which node connects"""
        name = self.scanNodeName(scanner)
        if name is None:
            print("Missing node name")
        else:
            node = self.graph.findNode(name)
            if node is None:
                print("No node named " + name)
            else:
                for arc in node.getArcs():
                    print(arc.getFinish())

    def bfsCommand(self, scanner):
        """bfs node -- Conducts a breadth-first search starting at node"""
        name = self.scanNodeName(scanner)
        if name is None:
            print("Missing node name")
        else:
            node = self.graph.findNode(name)
            if node is None:
                print("No node named " + name)
            else:
                bfs(node, print)

    def dfsCommand(self, scanner):
        """dfs node -- Conducts a depth-first search starting at node"""
        name = self.scanNodeName(scanner)
        if name is None:
            dfs(self.graph, print)
        else:
            node = self.graph.findNode(name)
            if node is None:
                print("No node named " + name)
            else:
                dfs(node, print)

    def hopsCommand(self, scanner):
        """hops node -- Prints a breadth-first search including hop counts"""
        def printNameAndDistance(node, distance):
            print(node.getName() + " " + str(distance))
        name = self.scanNodeName(scanner)
        if name is None:
            print("Missing node name")
        else:
            node = self.graph.findNode(name)
            if node is None:
                print("No node named " + name)
            else:
                bfs(node, printNameAndDistance)

    def sortCommand(self, scanner):
        """sort -- Displays a topological sort of the graph"""
        def addToTimeline(node, timestamp):
            sequence.insert(0, node)
        sequence = [ ]
        dfs(self.graph, finish=addToTimeline)
        for node in sequence:
            print(node)

    def timestampCommand(self, scanner):
        """timestamp -- Displays a depth-first search with timestamps"""
        nodes = [ ]
        discoveryTimes = { }
        finishTimes = { }
        def setDiscoveryTime(node, timestamp):
            nodes.append(node)
            discoveryTimes[node] = timestamp
        def setFinishTime(node, timestamp):
            finishTimes[node] = timestamp
        dfs(self.graph, setDiscoveryTime, setFinishTime)
        for node in nodes:
            print(str(node) + "<" + str(discoveryTimes[node]) + ":" +
                                    str(finishTimes[node]) + ">")

# Private functions

    def scanNodeName(self, scanner):
        """Reads the name of a node from the scanner."""
        token = scanner.nextToken()
        ttype = scanner.getTokenType(token)
        if ttype == TokenScanner.EOF:
            return None
        elif ttype == TokenScanner.WORD or ttype == TokenScanner.NUMBER:
            return token
        elif ttype == TokenScanner.STRING:
            return scanner.getStringValue(token)

# Startup code

if __name__ == "__main__":
    GraphConsoleTest()
