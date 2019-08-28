#Combinations function: C(n,k) where you choose a k element subset from a set of n elements.
#You can find the value of thsi by lookign up an entry in pascals triangle.
#No calling for fact? factorial

##BELOW CURRENTLY JUST CREATES PASCALS TRIANGLE
def combinations(n, k): #get a set of n elements, shift right by k spots in that

    if k==0 or n == k: #If on boarders or at the very top of pyramid
        return 1
    else:
        return(combinations(n-1,k-1) + combinations(n-1,k)) #Return recursively all the numbers to hopefully get the number we need?
