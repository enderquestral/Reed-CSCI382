# File: pqueue.py

"""
This module implements the priority queue abstraction using a heap to
represent a partially ordered tree in which every node is smaller
than either of its children.  Maintaining this property during add
and remove operations requires log N time.
"""

from array import Array

class PriorityQueue:
    """
    This class implements a queue structure whose elements are
    removed in priority order.  As in conventional English usage,
    lower priority values are removed first.  Thus, priority 1
    items come before priority 2.
    """

    def __init__(self):
        """Creates an empty priority queue."""
        self._capacity = PriorityQueue.INITIAL_CAPACITY
        self._array = Array(self._capacity)
        self._dict = {}
        self._count = 0
        self._timestamp = 0

    def __contains__(self, key):
        #iterate through, try and find key
        return key in self._dict
            
    

    def size(self):
        """Returns the number of values in this queue."""
        return self._count

    def isEmpty(self):
        """Returns True if this queue contains no elements."""
        return self._count == 0

    def clear(self):
        """Removes all elements from this queue."""
        self._count = 0

    def enqueue(self, value, priority=0):
        """Adds value to this queue using the specified priority."""
        if self._count == self._capacity:
            self._expandCapacity()
        array = self._array
        index = self._count
        self._count += 1
        self._timestamp += 1
        entry = PriorityQueue._PQEntry(value, priority, self._timestamp)
        self._array[index] = entry
        while index > 0:
            parent = (index - 1) // 2
            if array[parent] < array[index]:
                self._dict[value] = index ## priortity
                break
            array[parent],array[index] = array[index],array[parent]
            index = parent
        if index == 0:
            self._dict[value] = 0 ## priority


    def dequeue(self):
        """Removes the first element from this queue and returns it."""
        if self._count == 0:
            raise IndexError("dequeue called on an empty queue")
        array = self._array
        value = array[0]._value
        self._count -= 1
        array[0] = array[self._count]
        index = 0
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            if left >= self._count:
                break
            child = left
            if right < self._count and array[right] < array[left]:
                child = right
            if array[index] < array[child]:
                break
            indexkey = array[index]._value ##
            childkey = array[child]._value ##
            array[child],array[index] = array[index],array[child]
            self._dict[indexkey] = child ##
            self._dict[childkey] = index ##
            index = child
        return value

    def peek(self):
        """Returns the first item in the queue without removing it."""
        if self._count == 0:
            raise IndexError("peek called on an empty queue")
        return self._array[0]._value

    def peekPriority(self):
        """Returns the priority of the first item in the queue."""
        if self._count == 0:
            raise IndexError("peekPriority called on an empty queue")
        return self._array[0]._priority
    def raisePriority(self, value, newPriority):
        """Raises the priority of the specified value to newPriority."""
        def findValue(v):
            index = self._dict[v]
            if index == None:
                raise ValueError("Illegal priority in raisePriority")
            return index 

        #"add enqueued nodes to a dictionary inside priority queue and dequeue them from that dictionary"

        array = self._array
        index = findValue(value)
        if array[index]._priority < newPriority:
            raise ValueError("Illegal priority in raisePriority")
        array[index]._priority = newPriority

        while index > 0:
            parent = (index - 1) // 2
            if array[parent] < array[index]:
                break
            array[parent],array[index] = array[index],array[parent]
            index = parent


    def raisePriorityOrig(self, value, newPriority):
        """Raises the priority of the specified value to newPriority."""
        def findValue(value):
            for i in range(self._count):
                if array[i]._value == value:
                    return i
            raise ValueError("raisePriority called with nonexistent value")
        #   When visiting neighbors of vertex, insert them into heap no matter if they in heap or not. 
        #When gotten vertex w/ smallest distance from heap, check if it has been removed from heap before. 
        #If yes, remove this one and continue. Else, mark as removed and visiv all neighbors.

        array = self._array
        index = findValue(value)
        if array[index]._priority < newPriority:
            raise ValueError("Illegal priority in raisePriority")
        array[index]._priority = newPriority
        while index > 0:
            parent = (index - 1) // 2
            if array[parent] < array[index]:
                break
            array[parent],array[index] = array[index],array[parent]
            index = parent

# Implementation notes: _expandCapacity
# -------------------------------------
# The expandCapacity method allocates a array of twice the previous
# size, copies the old elements to the array, and then replaces the
# old array with the one.

    def _expandCapacity(self):
        self._capacity *= 2
        newArray = Array(self._capacity)
        for i in range(self._count):
            newArray[i] = self._array[i]
        self._array = newArray

# Constants

    INITIAL_CAPACITY = 10

# Implementation notes: _PQEntry
# ------------------------------
# This private class combines three values: a value, a priority,
# and a timestamp.  The timestamp is used to break ties between
# items of equal priority and therefore ensures that such items
# obey the standard first-in/first-out queue discipline.  This
# class implements the less-than operator to simplify priority
# comparisons.

    class _PQEntry:
        def __init__(self, value, priority, timestamp):
            self._value = value
            self._priority = priority
            self._timestamp = timestamp
        def __lt__(self, other):
            if self._priority < other._priority:
                return True
            if self._priority > other._priority:
                return False
            return self._timestamp < other._timestamp
