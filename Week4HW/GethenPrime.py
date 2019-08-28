#Problem 5. Species Determination on Gethen Prime
#Worked on this with Ariel Flaster and Jirarong Li

#part a. Uses O(nlogn) calls to isSameSpecies

def isSameSpecies(alien1, alien2):
    if alien1 == alien2:
        return True
    return False


def findAlienMajorityA(array):
    if len(array)==1:
        return array[0]
    else:
        left = findAlienMajorityA(array[:n/2]) #divide groups into 2
        right = findAlienMajorityA(array[n/2:])
        if isSameSpecies(left, right):
            return left
        else:
            if left == null AND right == null:
                return null
            elif left == null AND right != null:
                return right
            elif left != null AND right == null:
                return left
            else:
                leftcounter = 0
                rightcounter = 0
                for i in range(len(array)):
                    if isSameSpecies(left, array[i]):
                        leftcounter +=1
                    elif isSameSpecies(right, array[i]):
                        rightcounter +=1
                if leftcounter > rightcounter:
                    return left
                elif rightcounter >leftcounter:
                    return right
                else: #leftcounter == rightcounter
                    return null


#part b

