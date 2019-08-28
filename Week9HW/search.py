# File: search.py
# Author: CLRS/ Eric Robers
# Commentor: Hannah Hellerstein
#
# An implementation of the Boyer-Moore string matching algorithm. This algorithm takes a text string, and a pattern string which needs to be found within the text string. Finding the first occurrence of the pattern within the text has a worst case running time of O(n+m), only if the pattern is not in the text and O(nm) if it is (n being the length of the pattern and m being the length of the text).
#
# One thing that is crucial about Boyer-Moore is that we compare the pattern to the text, starting at the ending character 
# of the pattern and moving towards the beginning character. 
# That way, it allows for more efficient shifting (and thus fewer comparisons) of the pattern along the text, 
# skipping ahead or behind as necessary depending on where the prior mismatch happened, and with what latter. 
#
# The Boyer-Moore string-search algorithm is dependant on bad-character formatting, 
# which forms a series of conditions of how the pattern should be shifted along the text, depending on where 
# the mismatch between the text and pattern happened, and with what characters. 
# If the mismatch happened with a character that isn’t in the pattern, you know that the next place to search 
# is at least (pattern length) away from the mismatch. 
# If that’s not the case, then the pattern is shifted ahead by the appropriate number of spaces. 
# The appropriate number of spaces often depends on when when in the pattern the mismatch occurred, 
# and how far along the pattern would have to shift for that text character to appropriately line up with a 
# character in the pattern. In this implementation, we store the bad-character information within a dictionary, with 
# the pattern characters being the keys and the associated array containing the relevant shifts for a given index.
#
# For an example of bad-character formatting, temporarily consider the string “RTYRTORTRO” and the pattern “TTRRORT”. 
# We start at index 7 in both places, and move backwards. 
# ‘R’ and ‘T’ don’t match up, so we shift ahead by one. 
# ‘ORT’ and ‘ORT’ match, but ‘T’ and ‘R’ do not. We shift the pattern forward so there is a ‘T’ that matches with the strings ‘T’. 
# Sadly this pattern example is not in the text example but I hope my point is clear.
#
#The basic framework of the Boyer-Moore string-search algorithm is this:
#-   Initialize a bad character table off of the pattern. 
#    Do this by determining what it would take the pattern to shift by, in order to possibly match a character 
#    within the pattern to a character within the text.
#-   Loop so that while there is room for the pattern within the text given a starting point (often at 0), 
#    check to see if the pattern can be found. If all characters match, then return the number of shifts needed. 
#    Else, shift ahead by an amount specified by the bad character table, or by the length of the pattern.
#-   If you loop through the entire text and do not find the pattern, the pattern does not exist in the texts 
#    and so shifting is pointless. 


"""
This module implements a simplified version of the Boyer-Moore search
algorithm for strings that uses only the bad-character rule.  Detailed
comments have been omitted intentionally to create a useful exercise
in documentation.
"""


# Function: findString(text, pattern, start)
# Usage: findString("bacbababaabcbab", "bcbab") #Returns a number, tx (10 in this case), that is the number of shifts needed to find the pattern in the text.
# -----------------------------------------------------------------------------
# Uses the Boyer-Moore algorithm to find a given pattern string in a larger text string. 
# To do this, we create a bad character table, which is done in initBadCharacterTable below. 
# We also need to keep in mind the length of the text string and the length of the pattern string. 
# We also need to take “the expected number of spaces we will shift away from point 0”, defaulting to 0. 
# While there is enough “unexplored” room in the text string, we compare characters. 
# Starting at the rear of the pattern, if each character in the pattern matches up with the paired character in the text, 
# then we have found the patterns location and can return the number of shifts. 
# Else, we change the shift number differently depending on if the mismatched character in the text is in the bad character 
# table. If it’s not, then we shift ahead by the entirety of the pattern length. 
# If it is, then we change the shift by the difference between the number of non-matching characters with the last comparison, 
# and the associated value in the bad character table for that number and mismatched text character. 
# If the algorithm fails to find the pattern in the string, -1 is returned.


def findString(text, pattern, start=0):
    bct = initBadCharacterTable(pattern) 
    #Get the character table for the characters in pattern. 
    #This gives a bad character table for the pattern.

    #Get the size of the text you're comparing against
    n = len(text) 
    #Get the size of the pattern
    m = len(pattern) 
    #Assign the "expected number of shifts away from position 0" to tx. 
    tx = start  

    while tx <= n - m:
        px = m - 1 #Make px be the length of the pattern-1, for better use indexing in an array.

        #If the letter at spot px matches a given spot in the text, subtract px by one.
        #Within this loop, if px <= -1, then all the characters in the pattern match.
        #tx is returned, giving the amount of shifts over from position 0 for the associated match.
        while pattern[px] == text[tx + px]:
            px -= 1
            if px == -1:
                return tx

        #If the character at the spot [tx + px] in the text exists in the bad character table,
        #change tx by whatever px is, minus the associated value in the bad character table.
        if text[tx + px] in bct:
            tx += px - bct[text[tx + px]][px]

        #If the character in the string is not in the bad character table, then just change tx by adding the length of the pattern,
        #skipping ahead in the text by the length of the pattern. 
        else:
            tx += m
    #Finally, if the pattern DOES NOT EXIST in the text, return -1.
    return -1

# Function: initBadCharacterTable(pattern)
# Usage: print(initBadCharacterTable("bcbab")) #prints {'b': [-1, 0, 0, 2, 2, 4], 'c': [-1, -1, 1, 1, 1, 1], 'a': [-1, -1, -1, -1, 3, 3]}
# -----------------------------------------------------------------------------
# Builds a dictionary of values that a pattern should shift by, if the character of the text being searched doesn’t 
# match with the associated character of the pattern. 
# Each character in the pattern has its own set of numbers to shift by, depending at what point in the comparison 
# the mismatch occurred. We get this dictionary by counting out the unique characters in the pattern, initializing 
# them all to -1. 
# You then fill out the character entries in the dictionary by looping through 0 to the length of the pattern-1, 
# appending the loop iteration number to the character dictionary if the character matches the character found at 
# that iteration spot in the pattern. 
# If that isn’t the case, you instead append the previous “rear” value in that character dictionary again.

def initBadCharacterTable(pattern):
    #Take m as the length of the pattern.
    m = len(pattern) 
    #Initialize an array with a -1, for every unique character in the pattern. This will be our bad character table.
    bct = { ch:[-1] for ch in pattern } 

    #At this point, we loop through the length pattern, with i being our location marker. 
    #Each time we loop, we check each character in the bad character table.
    #If the character in the bad character table is the same as the character at the position i in the pattern, 
    #then we append the value i to the associated charater in the bad character table.
    #However, if the character in the bad character table does not match the character at position i in the pattern, 
    #then we append the value at position i within the associated character array to the same character array.
    #This effectively just copies what was in the previous end spot again.

    #After we finish all the looping, we return the bad character table array. 
    for i in range(0, m):
        for ch in bct:
            if ch == pattern[i]:
                bct[ch].append(i)
            else:
                bct[ch].append(bct[ch][i])
    return bct

def goodSuffixRule(pattern):
    gst = { ch:[-1] for ch in pattern } 
    m = len(pattern)
    holdstring = ""
    for i in range(0,m):
        for q in range(1,m+1):
            messwiththis = True
            for z in range(0, len(holdstring)):
                term_index = q-len(holdstring)-1+z
                if term_index <0 or holdstring[z] == pattern[term_index]:
                    pass
                else:
                    messwiththis = False
            term_index =q-len(holdstring)-1
            if messwiththis and (term_index <=0 or pattern[term_index-1] != pattern[m-1-i]):
                return m-q+1
        holdstring = pattern[m -1 -i] + holdstring
    return gst

# Test program

#The 'main' of this file. Has several test cases that are fed through runOneTest. Runs upon file startup.
def TestSearch():
    runOneTest("bacbababaabcbab", "abaab", 6);
    runOneTest("bacbababaabcbab", "ab", 4);
    runOneTest("bacbababaabcbab", "bcbab", 10);
    runOneTest("bacbababaabcbab", "xyzzy", -1);

#Takes inputs of a text string, a pattern string to find in the text string, and a number of expected shifts the search would take.
#Prints out a string of what findString outputs given a text and pattern.
def runOneTest(text, pattern, expected):
    print("findString(\"" + text + "\", \"" + pattern + "\") -> " +
          str(findString(text, pattern)) +
          " (should be " + str(expected) + ")")

# Startup code

if __name__ == "__main__":
    TestSearch()
