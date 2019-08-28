
from PriorityQueue import PriorityQueue


def PriorityQueueTest():
    errorcount = 0
    q = PriorityQueue()
    #UnitTest.assertTrue("q.isEmpty() -> " + str(q.isEmpty()), q.isEmpty())
    if q.isEmpty() != True:
        errorcount +=1
    if len(q) != 0:
        errorcount +=1

    q.enqueue("Kokichi", 10);
    q.enqueue("Gonta", 9);
    q.enqueue("Kirumi", 4);
    q.enqueue("Kaede", 2);
    q.enqueue("Miu", 8);
    q.enqueue("Kaito", 11);
    q.enqueue("Ryoma", 3);
    q.enqueue("Korekiyo", 7);
    q.enqueue("Rantaro", 1);
    q.enqueue("Angie", 5);
    q.enqueue("Tenko", 6);
    
    ###TEST STUFF HERE###
    
    if q.isEmpty():
        errorcount +=1
    if len(q) != 11:
        errorcount +=1

    line = []
    while not q.isEmpty():
        #print(q.printout())
        #print(q.dequeue())
        line.append(q.dequeue())
        #print(q.printout())
        #print(len(q))
        #print(" ")
    for i in range(len(line)):
        if i+1 != line[i][1]: #checks to see if the priority does indeed go from min(1) to max(11) values
            errorcount +=1



    if q.isEmpty() != True: #makes sure that after dequeueing all of that, q is empty
        errorcount +=1
    if len(q) != 0:
        errorcount +=1

    

    #Testing out cases where the priorities are not numerically right after the other
    q.enqueue("Keebo", 11);
    q.enqueue("Tsumugi", 3);
    q.enqueue("Shuichi", 7);
    q.enqueue("Himiko", 1);
    q.enqueue("Maki", 5);


    line = []
    while not q.isEmpty():
        #print(q.printout())
        #print(q.dequeue())
        line.append(q.dequeue())
        #print(q.printout())
        #print(len(q))
        #print(" ")
    
    #print(line)
    lastpriority = line[0][1]
    for i in range(1, len(line)):
        if lastpriority > line[i][1]:#checks to see if the priority of outputs still is from min to max
            errorcount +=1
        lastpriority = line[i][1]


    q.enqueue("Monokid", 11); #Just adding values to make sure the .clear() function works...
    q.enqueue("Monodam", 3);
    q.enqueue("Monophanie", 7);
    q.enqueue("Monokuma", 1);
    q.enqueue("Monosuke", 6);
    q.enqueue("Monotaro", 5);
    q.enqueue("Nanokumas", 10);

    q.clear() #Test to see if .clear() works
    if len(q) != 0:
        errorcount +=1
    if q.isEmpty() != True:
        errorcount +=1

    if (errorcount == 0):
        print("PriorityQueueTest succeeded")
    else:
        print("PriorityQueueTest failed")



if __name__ == "__main__":
    PriorityQueueTest()
