
#Worked with Casey Harris on this one

def isMeasurable(target, weights): #Weights is a list of different numbers
    if target== sum(weights):
        return True
    for w in range(len(weights)):
        if isMeasurable(target+w, weights[:w] +weights[w+1:]): #adding w to target
            return True #recursive call within it
        if isMeasurable(target-w, weights[:w] +weights[w+1:]): #putting w on not-target side
            return True
        if isMeasurable(target, weights[:w] +weights[w+1:]):#Don't touch it
            return True
    return False

