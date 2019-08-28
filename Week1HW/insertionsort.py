#Written by: Hannah Hellerstein 
#Collaboration with: Casey Harris


def sort(list): #exports this function?
    #implemented using insertion-sort algorithm in chapter 1 of intro to algorithms textbook

    #for j=2 to list.length
    #key = list[j]
    # //insert list[j] into the sorted sequence list[1,,,j-1]
    #i = j-1
    #while i>0 and list[i] >key:
    #   list[i+1] = list[i]
    #   i=i-1
    # list[i+1]=key

    #j=2
    for j in range(1, len(list)):
        key = list[j]

        #insert list[j] into the sorted sequence list[1,,,j-1]
        i = j-1
        while i>=0 and list[i] > key:
            list[i+1] = list[i]
            i-=1
        list[i+1] = key
    
    #return list


