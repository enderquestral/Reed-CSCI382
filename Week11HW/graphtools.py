# File: graphtools.py

"""
This module defines the following tools for graphs:

  readGraphData(g, file)  Loads graph data from the specified file
  bfs(start, fn)          Conducts a breadth-first search from start
  dfs(start, fn)          Conducts a depth-first search from start
  dfs(g, fn)              Applies depth-first search to the entire graph
"""

from graph import Graph, Node, Arc
from tokenscanner import TokenScanner
from inspect import signature

# Implementation notes: readGraphData
# -----------------------------------
# This function makes two passes over the data file, a "prescan" phase
# that defines the nodes names and a "scan" phase that rereads the data,
# interprets any options, and then updates the graph structure.  The
# purpose of this design is to allow the same data files to work with
# different graph representations, some of which require the nodes to
# be defined before processing the arc information.

def readGraphData(g, filename):
    """
    Reads graph data from the specified file.  The lines in the file
    take one of two forms: (1) a node specification containing the
    name of the node or (2) an arc specification that includes two
    node names separated either by an operator indicating the type
    of the arc.  The operator -> specifies a directed arc, and the
    operator - specifies an undirected arc, which is implemented as
    one arc in each direction.  Either form may be followed in the
    file by an option string enclosed in parentheses, which is used
    to initialize the attributes of the specific Node or Arc subclass.
    The format of these option strings is defined by the subclass.
    """
    scanner = TokenScanner()
    scanner.ignoreWhitespace()
    scanner.scanNumbers()
    scanner.scanStrings()
    scanner.addOperator("->")
    for phase in ["prescan", "scan"]:
        with open(filename) as f:
            for line in f:
                line = line.strip()
                if line != "" and not line.startswith("#"):
                    scanner.setInput(line)
                    n1 = g.addNode(scanNodeName(scanner))
                    token = scanner.nextToken()
                    if token == "-" or token == "->":
                        op = token
                        n2 = g.addNode(scanNodeName(scanner))
                        token = scanner.nextToken()
                    else:
                        op = None
                    if phase == "scan":
                        options = None
                        if token == "(":
                            p1 = scanner.getPosition()
                            p2 = line.rfind(")")
                            options = line[p1:p2]
                        if op is None:
                            if options is not None:
                                n1.scanOptions(options)
                        else:
                            arc = g.addArc(n1, n2)
                            if options is not None:
                                arc.scanOptions(options)
                            if op == "-":
                                arc = g.addArc(n2, n1)
                                if options is not None:
                                    arc.scanOptions(options)

def scanNodeName(scanner):
    """Reads the name of a node from the scanner."""
    token = scanner.nextToken()
    ttype = scanner.getTokenType(token)
    if ttype == TokenScanner.WORD:
        return token
    elif ttype == TokenScanner.STRING:
        return scanner.getStringValue(token)

# Implementation notes: Traversal functions
# -----------------------------------------
# The two standard traversal functions, dfs and bfs, take callback
# functions that are applied to the node.  In each case, however,
# the implementation uses inspection to determine whether the
# callback function requires additional keyword parameters that
# are appropriate to that traversal.

def dfs(start, fn=None, finish=None):
    """
    Conducts a depth-first search of the graph, beginning at start.
    If fn is supplied, it is called on each node as it is visited.
    If finish is supplied, it is called after completing the
    recursive exploration of this node.  For each of the fn and
    finish callback functions, the first argument is the node.
    The implementation also checks to see whether the function
    takes a parameter named "timestamp"; if so, that parameter
    is passed as a keyword argument.
    """
    def innerDFS(node):
        nonlocal t
        if node not in visited:
            t = t + 1
            if fn is not None:
                kwargs = { }
                if hasNamedParameter(fn, "timestamp"):
                    kwargs["timestamp"] = t
                fn(node, **kwargs)
            visited.add(node)
            for arc in node.getArcs():
                innerDFS(arc.getFinish())
            t = t + 1
            if finish is not None:
                kwargs = { }
                if hasNamedParameter(finish, "timestamp"):
                    kwargs["timestamp"] = t
                finish(node, **kwargs)
    visited = set()
    t = 0
    if isinstance(start, Node):
        innerDFS(start)
    elif isinstance(start, Graph):
        for node in start.getNodes():
            innerDFS(node)

# Implementation note: bfs
# ------------------------
# The extra information for distance and predecessor described in CLRS
# is maintained here in dictionaries indexed by node.  The reason for
# doing so is to avoid having the bfs function make changes to the
# Node objects, which are conceptually in the client's domain.

def bfs(start, fn=None):
    """
    Conducts a breadth-first search of the graph, beginning at start.
    If fn is supplied, it is called on each node as it is visited.
    The standard parameter to the callback function is the node, but
    two others (distance and predecessor) are supplied as keyword
    parameters if the callback function defines them.
    """
    visited = { start }
    queue = [ start ]
    distances = { start: 0 }
    predecessors = { start: None }
    while len(queue) > 0:
        node = queue.pop(0)
        if fn is not None:
            kwargs = { }
            if hasNamedParameter(fn, "distance"):
                kwargs["distance"] = distances[node]
            if hasNamedParameter(fn, "predecessor"):
                kwargs["predecessor"] = predecessors[node]
            fn(node, **kwargs)
        for arc in node.getArcs():
            finish = arc.getFinish()
            if finish not in visited:
                distances[finish] = distances[node] + 1
                predecessors[finish] = node
                queue.append(finish)
                visited.add(finish)

def hasNamedParameter(fn, name):
    try:
        for param in signature(fn).parameters:
            if param == name:
                return True
    except ValueError:
        pass
    return False
