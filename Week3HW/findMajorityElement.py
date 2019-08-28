#Written by Hannah Hellerstein
#Written in collaboration with Casey Harris

def findMajorityElement(array):
    #Takes an array of nonnegative ints and returns the majority element, which is a value that occurs in at least 50%+1 of the element positions.
    #If not majority element exists, function should return -1.

    #MUST mon in O(N) time, so can only search through array once
    #It may use indiv temp variables, may not allocate additional array storage. NO RECURSION.
    #No changing values in the array. 
    count = 0
    majorityelement = 0 #Getting variables is O(1)

    for i in array: #Loops through array size once, is O(N)
        if count == 0:
            majorityelement = i
            
        if i == majorityelement:
            count+=1
        else:
            count-=1
    #JUST get candidate here


    majcount=0
    for x in array:# Loops through array size twice now, is 2O(N)... which get rid of const multipliers on the outside, is O(N)?
        if x == majorityelement:
            majcount +=1

    if majcount >= (len(array)//2)+1: #Getting the len(array) is O(1)
        return majorityelement

    return -1
    