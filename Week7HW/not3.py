def not3(a,b,c):
    #Use at max 2 not statements
    #return (not a, not b, not c)
    #NO CONTROL STRUCTURES, FUNCTION CALLS, OR OPERATORS ALLOWED
    all3 = a and b and c #true iff only all 3 are true
    ab = (a and b) #true if a,b are true
    ac = (a and c) #true if a,c are true
    bc = (b and c) #true if b,c are true
    part1 = not(ab  and  ac  and  bc) #FIRST NOT USE. Is false iff all 3 are True, returns true if at least 1 input is false
    part2 = not((all3 and part1)  and  all3) #SECOND NOT USE

    notA = ((bc and part2)and part1)  and  (bc and part2) 
    notB = ((ac and part2)and part1)  and  (ac and part2)
    notC = ((ab and part2)and part1)  and  (ab and part2)
    return (notA, notB, notC)

