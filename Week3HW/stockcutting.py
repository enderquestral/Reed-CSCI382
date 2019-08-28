
def cutStock(requests, stockLength): #List of requested pipe length, length of stock pipe that distributor sells
    #returns minimum number of stock pipes needed to service all requests in the list. 
    #May assume that all requests are positive, do not exceed stock length. Worst case, need N stock pipes, N being list size
    #Do not need to report how to cut the pipes, just # of pipes needed
    #Use cutStock as wrapper function, so can take additional elements?
    #Hint: given current state and a request, what options are available for satisfying that request & how does that change the state?
    #Making a choice should result in a smaller subproblem to be recursively solved.

    #Size of remnants does not matter, just limit how many remnants there are. 
    #How to figure out how to fill first request? First request has to come from new pipe
    #new requests can come from any past remnants

    #PSEUDOCODE
    #LOOK AT ALL POSSIBILITIES FOR FIRST REQUEST
    #CHECK RECURSIVELY HOW MANY PIPES ARE NEEDED
    #RETURN SMALLEST

    #Like n queens problem? or maze problem, but keep going after finding one solution keep going to find shortest solution

    #####
    
    #recursive version
    def getListOfCuttingOptions(requests, stockLength, remnants):
        cuttingoptions = []
        if requests != []: ##if requests is not empty
            holdfirstoption = requests[0]
            for r in range((stockLength//holdfirstoption)+1): #reduce the length so at max its stockLength +1, and min its 2
                newlengthtouse = stockLength - (r*holdfirstoption) #Reduce the stockLen for a given moment
                tempremnants = remnants[:]#copy every element in remnants
                tempremnants.append(r) #get a remnant of size r, that can be taken from the difference between stockLength and holdfirstoption?
                cuttingoptions.extend(getListOfCuttingOptions(requests[1:], newlengthtouse, tempremnants))
        else:
            cuttingoptions = [remnants]
        return cuttingoptions

    def findNumPipesNeeded(listofsolutions, requests, stockLength):
        holdtempminvalue = len(requests)
        for i in listofsolutions:
            #Need to make sure that the patterns can cover all the items
            #print(i)
            if sum(requests) <= (sum(i)*stockLength):
                if sum(i) < holdtempminvalue:
                    holdtempminvalue = sum(i)

        return holdtempminvalue

    #Nonrecursive version.
    def tryArrayOfStockLength(requests, stockLength, remnants):#get a [] of n10s. subtract i in requests, if you get a - or 0, hop to next
        
        spotinnewarray = 0
        if requests != []:
            for j in range(len(requests)):
                if (remnants[spotinnewarray] - requests[j]) == 0:
                    remnants[spotinnewarray] -= requests[j]
                    spotinnewarray+=1
                else:
                    if (remnants[spotinnewarray] - requests[j]) < 0:
                        spotinnewarray +=1
                        remnants[spotinnewarray] -= requests[j]
                    else:
                        remnants[spotinnewarray] -= requests[j]
        holdvalue = 0
        print(newarray)
        for x in newarray:
            if x != stockLength:
                holdvalue +=1
        return holdvalue
    #attempt at making the above recursive
    def tryArrayOfStockLength2(requests, stockLength, remnants):#get a [] of n10s. subtract i in requests, if you get a - or 0, hop to next
        
        spotinnewarray = 0
        holdvalue = 0
        if requests != []:
            #for j in range(len(requests)):
            if (remnants[spotinnewarray] - requests[0]) == 0:
                remnants[spotinnewarray] -= requests[0]
                spotinnewarray+=1
                return 1 + tryArrayOfStockLength(requests[1:], stockLength, remnants)
                #holdvalue += tryArrayOfStockLength(requests[1:], stockLength, remnants)
            else:
                if (remnants[spotinnewarray] - requests[0]) < 0:
                    spotinnewarray +=1
                    remnants[spotinnewarray] -= requests[0]
                    return 1 + tryArrayOfStockLength(requests[1:], stockLength, remnants)
                else:
                    remnants[spotinnewarray] -= requests[0]
                    holdvalue +=tryArrayOfStockLength(requests, stockLength, remnants)
            #holdvalue = 0
            #print(newarray)
            for x in remnants:
                if x != stockLength:
                    holdvalue +=1
            return holdvalue
        else:
            return 0

    def cutStockHelper(requests, stockLength, currentNumber):
        if requests == []:
            return 0 
        else:
            if currentNumber >= stockLength:
                subrequests = requests[1:]
                if subrequests != []:
                    return 1 + cutStockHelper(subrequests, stockLength, (currentNumber - stockLength)+subrequests[0])
                else:
                    return 1 + cutStockHelper(subrequests, stockLength, (currentNumber - stockLength))
            else:
                subrequests = requests[1:]
                return 1 + cutStockHelper(subrequests, stockLength,(currentNumber+subrequests[0]))

#### MAIN FUNCTION CODE BELOW ###
    #newarray = []
    #for i in range(len(requests)):
    #    newarray.append(stockLength)
    #return tryArrayOfStockLength(requests, stockLength, newarray)

    listofsolutions = getListOfCuttingOptions(requests, stockLength, [])
    print(listofsolutions)
    return findNumPipesNeeded(listofsolutions, requests, stockLength)

    #return cutStockHelper(requests, stockLength, requests[0])
    