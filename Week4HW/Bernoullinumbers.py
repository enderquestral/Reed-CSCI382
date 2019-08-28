import math 


def combinations(n, k): #get a set of n elements, shift right by k spots in that

    if k==0 or n == k: #If on boarders or at the very top of pyramid
        return 1
    else:
        return(combinations(n-1,k-1) + combinations(n-1,k)) #Return recursively all the numbers to hopefully get the number we need?


def BernoulliNumbers(number):#If not 1 and odd, is 0.00. 
    #Need to solve for B(n), which is part of the sum.... 
    if number == 0:
        return 1
    else:
        counter = 0
        for x in range(0,number): #From here on it sums up bernoullinumbers from range 0,number
            counter += combinations(number, x)*(BernoulliNumbers(x)/(number-x+1))#cant be //. Also can't use number+1 for combinations else we coult wind up with too much output.
            
        return 1-counter 

def printBernoulliNumbers():
    for x in range(11):
        getvalue = BernoulliNumbers(x)
        print("B("+str(x)+") = " + str(round(getvalue, 8)))
    
