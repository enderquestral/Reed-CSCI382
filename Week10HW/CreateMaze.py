# File: CreateMaze.py

from mazelib import Maze
from pgl import GWindow
import random

GWINDOW_WIDTH = 500
GWINDOW_HEIGHT = 300
MAZE_ROWS = 5
MAZE_COLS = 9
SQUARE_SIZE = 36


def CreateMaze2():
    g = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    maze = Maze(MAZE_ROWS, MAZE_COLS, SQUARE_SIZE)
    x = (g.getWidth() - maze.getWidth()) / 2
    y = (g.getHeight() - maze.getHeight()) / 2
    #createRandomMaze(maze)
    #g.add(maze, x, y)
    #g.setInterval(g.add(wall.setColor("Black")), 2000)
    walls = maze.getWalls()
    random.shuffle(walls)
    squares = maze.getSquares()
    for square in squares:
        square.setColor(randomColor())
    for wall in walls:
        updateMaze(maze, wall, g)


def updateMaze(maze, wall, graphics):
    sq1, sq2 = graphics.setInterval(wall.getSquares(), 2000)
    """walls = maze.getWalls()
                random.shuffle(walls)
                for wall in walls:"""
    sq1,sq2 = wall.getSquares()
    g1 = find(sq1)
    g2 = find(sq2)
    if g1 == g2:
        wall.setColor("Black")
    else:
        wall.setColor("White")
        union(sq1, sq2)

def CreateMaze():
    g = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)
    maze = Maze(MAZE_ROWS, MAZE_COLS, SQUARE_SIZE)
    x = (g.getWidth() - maze.getWidth()) / 2
    y = (g.getHeight() - maze.getHeight()) / 2
    createRandomMaze(maze)
    g.add(maze, x, y)

def createRandomMaze(maze):
    walls = maze.getWalls()
    random.shuffle(walls)
    squares = maze.getSquares()
    for square in squares:
        square.setColor(randomColor())
    for wall in walls:
        sq1,sq2 = wall.getSquares()
        g1 = find(sq1)
        g2 = find(sq2)
        if g1 == g2:
            wall.setColor("Black")
        else:
            wall.setColor("White")
            union(sq1, sq2)

#setLink and getLink used to hold the back pointers to the representative
def find(node):
    """Returns the representative of the set to which node belongs."""
    if node.getLink() == None: #If .getLink() is None, then node is representative
        return node
    if node.getLink() != node:
        node.setColor(node.getLink().getColor())
        node.setLink(find(node.getLink())) #Compresses the path
    return node.getLink() #If .getLink() is node, then we've found the proper representative


def union(n1, n2):
    """Combines the sets containing these nodes into a single set."""
    # Fill this in
    #Link(FindSet(x), FindSet(y))

    setof1 = find(n1)
    setof2 = find(n2)
    if setof1.getRank() > setof2.getRank():
        ##holdcolor = randomColor()
        setof2.setColor(setof1.getColor())
        #setof1.setColor(setof2)
        ##setof1.setColor(randomColor)
        ##setof2.setColor(randomColor)

        setof2.setLink(setof1)
    else:
        ##holdcolor = randomColor()
        #setof2.setColor(setof1)
        setof1.setColor(setof2.getColor())
        ##setof1.setColor(randomColor)
        ##setof2.setColor(randomColor)

        setof1.setLink(setof2)
        #print(setof1.getRank())
        #print(setof2.getRank())
        if setof1.getRank() == setof2.getRank():
            setof2.setRank(setof2.getRank()+1)


def randomColor():
    """
    Returns a random opaque color expressed as a string consisting
    of a "#" followed by six random hexadecimal digits.
    """
    str = "#"
    for i in range(6):
        str += random.choice(["0", "1", "2", "3", "4", "5", "6", "7",
                              "8", "9", "A", "B", "C", "D", "E", "F"])
    return str

# Startup code

if __name__ == "__main__":
    CreateMaze()
