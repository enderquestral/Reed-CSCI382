# File: array.py

"""
This file defines an Array class, which operates as a fixed-size
array that supports only the following operations:

- Creating an Array object with a specified fixed capacity
- Retrieving the capacity of the Array object
- Selecting the value of the element at a particular index
- Assigning a new value to the element at a particular index

Creating an Array of size n requires linear time; each of the
other operations runs in constant time.

The implementation of the Array class uses operator overloading
so that the selection operations use the same syntax as Python's
list class.
"""

class Array:
    """This class represents a fixed-length array."""

    def __init__(self, n):
        """Creates a new Array with n elements, each initialized to None."""
        self._list = [ None ] * n

    def capacity(self):
        """Returns the capacity of the Array, which remains fixed."""
        return len(self._list)

    def __getitem__(self, k):
        """Implements selection using bracket notation, as in array[i]."""
        return self._list[k]

    def __setitem__(self, k, value):
        """Implements assignment to an element, as in array[i] = value."""
        self._list[k] = value

    def __str__(self):
        """Converts an Array to its string representation."""
        return str(self._list)
