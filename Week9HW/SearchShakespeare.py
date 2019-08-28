# File: SearchShakespeare.py

"""
This program searches the entire Shakespeare canon for a string and
then prints the index and complete line of the first occurrence.
"""

from search import findString, initBadCharacterTable
from counter import Counter

def SearchShakespeare():
    with open("Shakespeare.txt") as f:
        text = f.read()
        n = len(text)
    pattern = input("Enter search string: ")
    counter = Counter()
    env = { "initBadCharacterTable": initBadCharacterTable }
    findWithCount = counter.patchFunction(findString, PATTERNS, env)
    index = findWithCount(text, pattern, 0)
    if index == -1:
        print("Not found.")
    while index >= 0:
        start = index;
        while start > 0 and text[start - 1] != "\n":
            start -= 1
        finish = index;
        while finish < n and text[finish] != "\n":
            finish += 1
        print(str(index) + ": " + text[start:finish])
        index = findWithCount(text, pattern, index + 1)
        print("Total character comparisons = " + str(counter.get()))

# Patterns for character comparisons

PATTERNS = [
    "pattern[px] == text[tx + px]"
]

# Startup code

if __name__ == "__main__":
    SearchShakespeare()
