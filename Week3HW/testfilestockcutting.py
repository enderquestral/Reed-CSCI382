def test1(requests, stockLength):
    def calculatePatterns(totalRollLength,lenOpts, head):
        """
        Recursively calculates the list of options lists for a cutting stock problem. The input
        tlist is a pointer, and will be the output of the function call.
        The inputs are:
        totalRollLength - the length of the roll
        lenOpts - a list of the sizes of remaining cutting options
        head - the current list that has been passed down though the recusion
        Returns the list of patterns
        """
        if lenOpts:
            patterns =[]
            #take the first option off lenOpts
            opt = lenOpts[0]
            for rep in range(int(totalRollLength/opt)+1):
                #reduce the length
                l = totalRollLength - rep*opt
                h = head[:]
                h.append(rep)
                patterns.extend(calculatePatterns(l, lenOpts[1:], h))
        else:
            #end of the recursion
            patterns = [head]
        return patterns 

    def howManyPipesNeeded(listofsolutions, requests, stockLength):
        holdtempminvalue = len(requests)
        for i in listofsolutions:
            #Need to make sure that the patterns can cover all the items
            if sum(requests) <= (sum(i)*stockLength):
                if sum(i) < holdtempminvalue:
                    holdtempminvalue = sum(i)
                
        return holdtempminvalue
    listofsolutions = calculatePatterns(stockLength, requests, [])
    return howManyPipesNeeded(listofsolutions, requests, stockLength)
