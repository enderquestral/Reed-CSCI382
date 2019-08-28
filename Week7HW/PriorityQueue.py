
class PriorityQueue:
    """
    PriorityQueue Class for Algorithms and Data structures class, 2019
    """
    def __init__(self):
        self._length = 0
        self._array = []
        #Except for the root at index 0, the node at index k has it's parent at (k-1)//2
        #Node at index k has its children at 2k+1(left) and 2k+2(right)

    def __len__(self): #returns number of elems
        return self._length

    def isEmpty(self): 
        return self._length == 0

    def clear(self):
        self._length = 0
        self._array = []

    def enqueue(self, value, priority): #Must run in o(log n) time
        #lower numeric values correspond to higher levels of urgency (priority 1 comes before a task with priority 2)
        newNodeIndex = self._length
        self._array.append((value, priority))
        self.resortit(newNodeIndex)
        self._length +=1

    def dequeue(self): #must run in O(Log n) time
        if self._length == 0: #NOTHING TO EXTRACT
            raise IndexError("Array is empty")
        result = self._array[0] #Takes "name" of first element, saves it
        emptyspaceindex = 0
        while (emptyspaceindex*2)+2 < self._length: #Should hopefully only run in O(Log n) time as only goes through part of the queue
            rightchild = (2*emptyspaceindex)+2
            leftchild = (2*emptyspaceindex)+1
            if (self._length <= rightchild and (leftchild < self._length)) or (self._array[leftchild][1] < self._array[rightchild][1]): 
                self._array[emptyspaceindex] = self._array[leftchild]
                emptyspaceindex = leftchild
            else:
                self._array[emptyspaceindex] = self._array[rightchild]
                emptyspaceindex = rightchild
        lastnodeindex = self._length-1
        self._array[emptyspaceindex] = self._array[lastnodeindex]
        self.resortit(emptyspaceindex)
        self._array.pop() #Removes element at the end of the list, which should be what was originally at the beginning, gets rid of it
        self._length -=1
        return result

### SECTION FOR PRIVATE/INTERNAL USE ###
    def printout(self): #Uses this to print out things, mostly used for bug testing/checking
        line = ""
        for i in range(self._length):
            line += str(self._array[i])
            line += ", "
        return line

    def resortit(self, newnodespot):
        while 1 <= newnodespot: #Should hopefully run in O(Log n), as the while loop divides in 2 each time
            newnode = self._array[newnodespot]
            parentindex = (newnodespot-1)//2
            parentnode = self._array[parentindex]
            if parentnode[1] < newnode[1]:
                break
            tempnode = parentnode
            self._array[parentindex] = newnode
            self._array[newnodespot] = tempnode
            newnodespot = parentindex
    

