# File: BadSearchCase.py

"""
This program counts the number of comparisons in the worst case for
naive search.
"""

from search import findString, initBadCharacterTable
from counter import Counter

def BadSearchCase():
    text = "a" * 200 + "b";
    pattern = "a" * 100 + "b";
    counter = Counter()
    env = { "initBadCharacterTable": initBadCharacterTable }
    findWithCount = counter.patchFunction(findString, PATTERNS, env)
    index = findWithCount(text, pattern, 0)
    if index == -1:
        print("Not found.")
    else:
        print("Found at index " + str(index))
    print("Total character comparisons = " + str(counter.get()))

# Patterns for character comparisons

PATTERNS = [
    "pattern[px] == text[tx + px]"
]

# Startup code

if __name__ == "__main__":
    BadSearchCase()
