from bst import BST

def isBalanced(bst):
    #returns true if the binary search tree bst is balances, false otherwise
    #bst is balances if:
    #1. The heights of its subtrees differ by no more than one
    #2. every subtree is itself balanced
    #THE REAL CHALLENGE: implement so that isBalanced determines the result without looking at any node more than once
    #bst is a BST

    def is_balanced_help(bst): #presuming I can't just access bst._root ...
        if bst.isEmpty():
            return 0
        left_node_height = 0
        right_node_height = 0

        if bst.getLeftSubtree() != None:
            left_node_height = is_balanced_help(bst.getLeftSubtree())
        if bst.getRightSubtree() != None:
            right_node_height = is_balanced_help(bst.getRightSubtree())
        
        if left_node_height == -1 or right_node_height == -1: #Checks to see if left or right subtrees are unbalanced.
            return -1

        if abs(left_node_height-right_node_height) >1: #checks to see height is not too tall
            return -1

        return max(left_node_height, right_node_height) + 1 #Tree should be balancedish here, return a value that is not -1

    return is_balanced_help(bst) != -1

def testIt():
    #This stree is unbalanced:
    newBST = BST()
    newBST.insert("testitroot", -2)
    newBST.insert("testitl", 0)
    newBST.insert("testitr", -1)
    newBST.insert("testitrl", 0)
    newBST.insert("testitrr", -1)
    newBST.insert("testitrrr", 0)

    print("the current tree is balanced: " + str(isBalanced(newBST))) #SHOULD RETURN FALSE

    #This tree should be balanced:
    newBST2 = BST()
    newBST.insert("testitroot", 7)
    newBST.insert("testitl", 3)
    newBST.insert("testitr", 11)
    newBST.insert("testitlr", 5)
    newBST.insert("testitll", 1)
    newBST.insert("testitrl", 9)
    newBST.insert("testitrr", 13)
    print("the current tree is balanced: " + str(isBalanced(newBST2))) #Should return True

    return 
