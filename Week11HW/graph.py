# File: graph.py

"""
This module defines the classes Graph, Node, and Arc, which are
used for working with graphs.
"""

class Graph:
    """Defines a graph as a set of nodes and a set of arcs."""

    def __init__(self):
        """Creates an empty graph."""
        self.clear()

    def clear(self):
        """Removes all the nodes and arcs from the graph."""
        self._nodes = { }
        self._arcs = set()

    def addNode(self, arg):
        """
        Adds a node to the graph.  The parameter to addNode is
        either an existing Node object or a string.  If a node is
        specified as a string, addNode looks up that string in the
        dictionary of nodes.  If it exists, the existing node is
        returned; if not, addNode creates a new node with that name.
        The addNode method returns the Node object.
        """
        if type(arg) is str:
            node = self.findNode(arg)
            if node is None:
                node = self.createNode(arg)
        elif isinstance(arg, Node):
            node = arg
        else:
            raise ValueError("Illegal node specification")
        self._nodes[node.getName()] = node
        return node

    def addArc(self, a1, a2=None):
        """
        Adds an arc to the graph.  The parameters to addArc are
        either a single Arc object or a pair of nodes, each of
        which can be an existing Node object or a string.  If a
        node is specified as a string, addArc looks up that name
        in the dictionary of nodes.  If it exists, the existing
        node is returned; if not, addArc creates a new node with
        that name.  The addArc method returns the Arc object.
        """
        if isinstance(a1, Arc) and a2 is None:
            arc = a1
        else:
            start = self.addNode(a1)
            finish = self.addNode(a2)
            arc = self.createArc(start, finish)
        self._arcs.add(arc)
        arc.getStart()._addArcFrom(arc)
        arc.getFinish()._addArcTo(arc)
        return arc

    def removeNode(self, arg):
        """ Removes a node from the graph. """
        #Argument can be either a node or a string representing the name of the node.
        #Removing a node means removing all arcs that refer to that node. 
        if type(arg) is str:
            node = self.findNode(arg)
            if node is None:
                raise ValueError("Illegal node specification")
        elif isinstance(arg, Node):
            node = arg
        else:
            raise ValueError("Illegal node specification")
        
        for n in self.getNodes():
            if n != node and node.isConnectedTo(n):
                self.removeArc(node, n)
        #node._arcsTo = set()
        #node._arcsFrom = set()
        #if node in self._nodes:
        #    raise ValueError("????h uh???")
        #graphnodes = self.getNodes()
        del self._nodes[node.getName()]


    def removeArc(self, a1, a2=None):
        """ Removes an arc from the graph. """
        #Arguments can be either a single Arc object or a pair of nodes, either as node objects or strings.
        #Removing an arc from a graph should leave the set of nodes unchanged, even if leaving an arc leaves a node isolated. 
        
        #if a1 and a2 are both arcs

        if a1 is None and a2 is None:
            raise ValueError("Illegal arc specification")
        else:
            if isinstance(a1, Arc) and a2 is None:
                arc = a1
            else: #Both a1 and a2 are nodes, either in string or node form
                if type(a1) is str:
                    node1 = self.findNode(a1)
                else:
                    node1 = a1
                if type(a2) is str:
                    node2 = self.findNode(a2)
                else:
                    node2 = a2
                if node1.isConnectedTo(node2):#Need to get an arc... without creating it. 
                    arc = None
                    for a in self._arcs:
                        if (a.getStart() == node1 and a.getFinish() == node2) or (a.getStart() == node2 and a.getFinish() == node1):
                            arc = a
            if arc == None:
                raise ValueError("Illegal arc specification")
                #Once arc was found in either case, go about process of removing arc from each node and the graph as a whole
            startnode = arc.getStart()
            endnode = arc.getFinish()
            

            if arc in startnode.getArcsFrom():
                startnode._arcsFrom.remove(arc)

            if arc in endnode.getArcsTo():
                endnode._arcsTo.remove(arc)
            ###
            #THIS SECTION BELOW IS TO GET RID OF A MULTI-DIRECTIONAL ARC.
            #Comment this section out if you just want to delete a bi-directional arc one way.

            antiArc = None #get the arc from endnode to startnode
            for m in endnode.getArcs():
                holdfinish = m.getFinish()
                if holdfinish == startnode:
                    antiArc = m
            if antiArc != None:
                startnode._arcsTo.remove(antiArc)
                endnode._arcsFrom.remove(antiArc)
                self._arcs.remove(antiArc)
            ###

            self._arcs.remove(arc)

    def findNode(self, name):
        """Returns the node with the specified name, or None."""
        return self._nodes.get(name)

    def getNodes(self):
        """Returns a sorted list of all the nodes in the graph."""
        return [ node for node in sorted(self._nodes.values()) ]

    def getArcs(self):
        """Returns a sorted list of all the arcs in the graph."""
        return [ arc for arc in sorted(self._arcs) ]

    def KahnsAlgorithm(self):
        #Works be choosing vertices in the same order as the eventual topological sort. 
        #First, find a list of "start nodes" which have no incoming edges and insert them into a set S, at lea
        emptyset = [] #L ← Empty list that will contain the sorted elements
        setofallwithnoedge = set()#S ← Set of all nodes with no incoming edge
        for x in self.getNodes(): #Get a node x from list of nodes
            if len(x.getArcsTo()) == 0:
                setofallwithnoedge.add(x)

        #print(setofallwithnoedge)
        #print(self.getArcs())
        #print(emptyset)

        while len(setofallwithnoedge) != 0:
            holdnode = setofallwithnoedge.pop()
            emptyset.append(holdnode.getName())
            holdarcs = holdnode.getArcsFrom()
            for e in holdarcs:
                m = e.getFinish()
                #del arc that starts at n and ends at m
                self.removeArc(holdnode, m)
                if len(m.getArcsTo()) == 0:
                    setofallwithnoedge.add(m)
        

        #print(setofallwithnoedge)
        #print(self.getArcs())
        #print(emptyset)

        if len(self.getArcs()) != 0:
            raise ValueError("GRAPH HAS AT LEAST ONE CYCLE")
        else:
            return emptyset
            

        #while S is non-empty:
        #    remove a node n from S
        #    add n to tail of L
        #    for each node m with an edge e from n to m do
        #        remove edge e from the graph
        #        if m has no other incoming edges then
        #            insert m into S
        #if graph has edges then
        #    return error   (graph has at least one cycle)
        #else 
        #    return L   (a topologically sorted order)


# Implementation notes: Factory methods
# -------------------------------------
# The factory methods createNode and createArc are called to
# create new nodes and arcs.  Clients who want to extend the
# operation of the Graph class do so by defining new subclasses
# for Graph, Node, and Arc and then override these factory
# methods to produce Node and Arc objects of the proper class.

    def createNode(self, name):
        """Returns a Node with the specified name."""
        return Node(name)

    def createArc(self, start, finish):
        """Returns a Arc between the specified nodes."""
        return Arc(start, finish)

# Overload standard methods

    def __str__(self):
        s = ""
        for arc in getArcs():
            if len(s) > 0:
                s += ", "
            s += str(arc)
        return "<" + s + ">"

    def __len__(self):
        return len(self._nodes)

# Implementation notes: Node class
# --------------------------------
# The Node class represents a single node in a graph, which is
# identified by a unique name.  Each Node object includes a list
# of the arcs that begin at that node.  The base class for Node
# defines no additional attributes, but clients can define new
# attributes for a node by creating a subclass and supplying
# the appropriate getters and setters.

class Node:

    def __init__(self, name):
        """Creates a graph node with the given name."""
        self._name = name
        self._arcsFrom = set()
        self._arcsTo = set()

    def getName(self):
        """Returns the name of this node."""
        return self._name

    def getArcs(self):
        """Equivalent to getArcsFrom (included for backward compatibility)."""
        return self.getArcsFrom()

    def getArcsFrom(self):
        """Returns a list of all the arcs leaving this node."""
        return [ arc for arc in sorted(self._arcsFrom) ]

    def getArcsTo(self):
        """Returns a list of all the arcs ending at this node."""
        return [ arc for arc in sorted(self._arcsTo) ]

    def getNeighbors(self):
        """Returns a list of the nodes to which arcs exist."""
        targets = set()
        for arc in self._arcsFrom:
            targets.add(arc.getFinish())
        return [ node for node in sorted(targets) ]

    def isConnectedTo(self, node):
        """Returns True if any arcs connects to node."""
        for arc in self._arcsFrom:
            if arc.getFinish() is node:
                return True
        return False

# Package methods called only by the Graph class

    def _addArcFrom(self, arc):
        """Adds an arc that starts at this node."""
        if arc.getStart() is not self:
            raise ValueError("Arc must start at the specified node")
        self._arcsFrom.add(arc)

    def _addArcTo(self, arc):
        """Adds an arc that finishes at this node."""
        if arc.getFinish() is not self:
            raise ValueError("Arc must end at the specified node")
        self._arcsTo.add(arc)

# Implementation notes: scanOptions
# ---------------------------------
# The scanOptions method is called by the utility function that
# reads a graph from a file whenever a node specification includes
# an options string enclosed in parentheses.  The format for that
# string will vary for different Node subclasses.  By default, the
# options string is ignored.  Subclasses that need to specify
# different attributes should overload this method so that the
# options string includes the information appropriate to the
# particular application.

    def scanOptions(self, options):
        """Scans the options string on a node definition line."""

# Overload standard methods

    def __str__(self):
        return self._name

# Implementation notes: Comparison operators
# ------------------------------------------
# The Node class defines the __lt__ and __le__ comparison
# functions so that nodes can be sorted.  The __gt__ and __ge__
# functions are defined implicitly because Python will
# automatically flip the order.  The comparison is based on the
# names of the nodes, which must be unique within a graph.

    def __lt__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        elif self is other:
            return False
        elif self._name < other._name:
            return True
        elif self._name > other._name:
            return False
        else:
            raise KeyError("Duplicate names in a graph")

    def __le__(self, other):
        return self is other or self < other

# Implementation notes: Arc class
# -------------------------------
# The Arc class represents a directed arc from one node to
# another.  The Arc class itself also defines an attribute called
# cost, which is used in many applications.  Clients can define
# new attributes for an arc by creating a subclass with the
# appropriate getters and setters.

class Arc:
    """This class defines a directed arc from one node to another."""

    def __init__(self, start, finish):
        """Creates an arc from start to finish."""
        self._start = start
        self._finish = finish
        self._cost = 0

    def getStart(self):
        """Returns the node at the start of the arc."""
        return self._start

    def getFinish(self):
        """Returns the node at the end of the arc."""
        return self._finish

    def setCost(self, cost):
        """Sets the cost attribute for the arc."""
        self._cost = cost

    def getCost(self):
        """Returns the cost attribute for the arc."""
        return self._cost

# Implementation notes: scanOptions
# ---------------------------------
# The scanOptions method is called by the utility function that
# reads a graph from a file whenever the arc specification
# includes an options string enclosed in parentheses.  The format
# for that string will vary for different Arc subclasses.  By
# default, the options string is a number, which is used to set
# the predefined cost attribute.  Clients that need to specify
# different attributes should overload this method so that the
# options string includes the information appropriate to the
# particular application.

    def scanOptions(self, options):
        """Scans the options string on an arc definition line."""
        cost = float(options)
        if cost == int(cost):
            cost = int(cost)
        self._cost = cost

# Overload standard methods

    def __str__(self):
        suffix = ""
        cost = self._cost
        if cost != 0:
            if cost == int(cost):
                cost = int(cost)
            suffix = " (" + str(cost) + ")"
        return str(self._start) + " -> " + str(self._finish) + suffix

# Implementation notes: Comparison operators
# ------------------------------------------
# The Arc class defines the __lt__ and __le__ comparison functions so
# that arcs can be sorted.  The __gt__ and __ge__ functions are defined
# implicitly because Python will automatically flip the order.  The
# comparison first compares the start nodes using the Node comparison
# order.  If the start nodes match, the comparison compares the finish
# nodes.  If those match as well, as they do in parallel arcs between
# the same pair of nodes, the comparison is based on the object id.

    def __lt__(self, other):
        if not isinstance(other, Arc):
            return NotImplemented
        elif self is other:
            return False
        elif self._start < other._start:
            return True
        elif self._start > other._start:
            return False
        elif self._finish < other._finish:
            return True
        elif self._finish > other._finish:
            return False
        else:
            return id(self) < id(other)

    def __le__(self, other):
        return self is other or self < other
