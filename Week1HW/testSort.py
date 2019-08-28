#Written by: Hannah Hellerstein 
#Collaboration with: Casey Harris
import insertionsort
import random
import time

def testSort(n): #input random int n
    #make sure n is an int
    start = time.perf_counter()
    listofints = []
    for x in range(0,n):
        listofints.append(random.randint(0,n))    #Creates a list of n random ints
    
    #for y in listofints:
    #    print(y)

    #Sorts the list by calling sort from insertionsort module
    insertionsort.sort(listofints)
    #checks to see if the resulting list is sorted into nondecreasing order, reporting an error if any elements are out of sequence. 
    
    #print(" ")
    #for y in listofints:
    #    print(y)
    if not all(listofints[y] <= listofints[y+1] for y in range(len(listofints)-1)): #something returned false
        print("ERROR SOMETHING IS OUT OF SEQUENCE")
        return
    

    elapsed = time.perf_counter() - start #Also, time this
    return elapsed

### Main run here ###

def main():
    #Write a Python program that measures the time required to sort a list for the following
    #values of n: 10, 100, 1000, 10000, and 100000
    holdtime = 0.0
    for x in range(1,10000):
        holdtime += testSort(10)
    holdtime = holdtime/10000
    print("The holdtime value for n = 10 is: " + str(holdtime))
    holdtime = 0.0

    for x in range(1,1000):
        holdtime += testSort(100)
    holdtime = holdtime/1000
    print("The holdtime value for n = 100 is: " + str(holdtime))
    holdtime = 0.0

    for x in range(1,100):
        holdtime += testSort(1000)
    holdtime = holdtime/100
    print("The holdtime value for n = 1000 is: " + str(holdtime))
    holdtime = 0.0

    for x in range(1,10):
        holdtime += testSort(10000)
    holdtime = holdtime/10
    print("The holdtime value for n = 10000 is: " + str(holdtime))
    holdtime = 0.0


    holdtime += testSort(100000)
    print("The holdtime value for n = 100000 is: " + str(holdtime))

    return

#Values I got: 
#The holdtime value for n = 10 is: 2.175475929834647e-05
#The holdtime value for n = 100 is: 0.0005289751240052283
#The holdtime value for n = 1000 is: 0.04531209654000122
#The holdtime value for n = 10000 is: 4.286054463999972
#The holdtime value for n = 100000 is: 515.8309603920006
