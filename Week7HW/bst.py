# File: bst.java

"""
This module exports a simple implementation of a binary search
tree (BST), which exports the following methods:

    BST()             -- Creates an empty binary search tree
    insert(key, data) -- Inserts key and sets its data field
    lookup(key)       -- Returns the BSTNode containing key, or None
    remove(key)       -- Removes the key from the tree, if present
    preorderWalk(fn)  -- Calls fn on every key in a preorder walk
    inorderWalk(fn)   -- Calls fn on every key in an inorder walk
    postorderWalk(fn) -- Calls fn on every key in a postorder walk

The insert, lookup, and remove methods run in O(log N) time if the
tree is balanced.  This implementation, however, does nothing to
maintain balance, so the performance will degrade to O(N).

In addition to the public methods described earlier, this implementation
of BST also exports the following methods, which allow clients to
determine the structure of the tree:

    isEmpty()         -- Returns True if the tree is empty
    getKey()          -- Returns the key in the root node
    getLeftSubtree()  -- Returns the left subtree
    getRightSubtree() -- Returns the right subtree

Methods that are useful to clients who understand the details of the
implementation are often classified as "friend" methods.
"""

# Implementation notes
# --------------------
# This implementation defines a BST as a structure containing a root,
# which is a reference to a BSTNode.  The empty tree is therefore not
# None but a reference to a structure that contains None as its root
# attribute.  The BSTNode class includes a data field, which is not
# used in the simple BST implementation, but is available to clients.

class BST:

    def __init__(self):
        """Creates an empty BST."""
        self._root = None

    def insert(self, key, data=None):
        """Inserts key into the BST and sets the data field."""
        if self._root is None:
            self._root = BSTNode(key, data)
        elif key == self._root._key:
            self._root._data = data
        elif key < self._root._key:
            self._root._left.insert(key, data)
        elif key > self._root._key:
            self._root._right.insert(key, data)

    def lookup(self, key):
        """Returns the BSTNode containing key or None if not found."""
        if self._root is None:
            return None
        elif key == self._root._key:
            return self._root
        elif key < self._root._key:
            return self._root._left.lookup(key)
        else:
            return self._root._right.lookup(key)

    def remove(self, key):
        """Removes key from the BST, if it is present."""
        if self._root is not None:
            if key == self._root._key:
                if self._root._left._root is None:
                    self._root = self._root._right._root
                elif self._root._right._root is None:
                    self._root = self._root._left._root
                else:
                    minKey = self._findMinimumKey(self._root._right)
                    self._root._key = minKey
                    self._root._right.remove(minKey)
            elif key < self._root._key:
                self._root._left.remove(key)
            else:
                self._root._right.remove(key)

    def preorderWalk(self, fn=print):
        """Calls fn on every key in a preorder walk."""
        if self._root is not None:
            fn(self._root._key)
            self._root._left.preorderWalk(fn)
            self._root._right.preorderWalk(fn)

    def inorderWalk(self, fn=print):
        """Calls fn on every key in an inorder walk."""
        if self._root is not None:
            self._root._left.inorderWalk(fn)
            fn(self._root._key)
            self._root._right.inorderWalk(fn)

    def postorderWalk(self, fn=print):
        """Calls fn on every key in a postorder walk."""
        if self._root is not None:
            self._root._left.postorderWalk(fn)
            self._root._right.postorderWalk(fn)
            fn(self._root._key)

# "Friend" methods

    def isEmpty(self):
        """Returns True if the tree is empty."""
        return self._root is None

    def getKey(self):
        """Returns the key in the root node."""
        return self._root._key

    def getLeftSubtree(self):
        """Returns the left subtree."""
        return self._root._left

    def getRightSubtree(self):
        """Returns the right subtree."""
        return self._root._right
    
# Private methods

    def _findMinimumKey(self, t):
        while t._root._left._root is not None:
            t = t._root._left
        return t._root._key

# Class: BSTNode

class BSTNode:

    def __init__(self, key, data=None):
        """Creates a new BST node with the specified key and optional data."""
        self._key = key
        self._data = data
        self._left = BST()
        self._right = BST()

    def getKey(self):
        """Returns the key in this BSTNode object."""
        return self._key

    def getData(self):
        """Returns the contents of the data field."""
        return self._data

    def setData(self, data):
        """Sets the contents of the data field."""
        self._data = data

    def __str__(self):
        if self._data is None:
            return "<" + self._key + ">"
        else:
            return "<" + self._key + ":" + self._data + ">"
