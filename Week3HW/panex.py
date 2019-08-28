# File: panex.py

"""
This module defines a library for maintaining the data structures for
the Panex puzzle and for displaying an image of the puzzle on the screen.
"""

import tkinter
# File: panex.py

"""
This module defines a library for maintaining the data structures for
the Panex puzzle and for displaying an image of the puzzle on the screen.
"""

import tkinter
import time
from pgl import GWindow, GRect, GPolygon, GCompound

# Constants

PIECE_WIDTH = 120
PIECE_HEIGHT = 40
PIECE_SEP = 1
COLUMN_SEP = 10
TOP_MARGIN = 10
BOTTOM_MARGIN = 10
SIDE_MARGIN = 10
CHANNEL_WIDTH = 14
LEFT_COLOR = "#0066FF"
RIGHT_COLOR = "#FF9900"
PIECE_COLOR = "#999999"
BORDER_COLOR = "#333333"
FRAME_COLOR = "#FFFFFF"
CHANNEL_COLOR = "#333333"
SLEEP_TIME = 0.1

# Class: PanexPuzzle

class PanexPuzzle(GWindow):

# Constructor

    def __init__(self, n):
        """Creates and displays a Panex puzzle with n levels."""
        self._nLevels = n
        self._frameWidth = 2 * SIDE_MARGIN + 3 * PIECE_WIDTH + 2 * COLUMN_SEP
        self._frameHeight = (TOP_MARGIN + BOTTOM_MARGIN +
                             (n + 1) * PIECE_HEIGHT + n * PIECE_SEP)
        GWindow.__init__(self, self._frameWidth, self._frameHeight)
        self._tk = tkinter._default_root
        self._tk.protocol("WM_DELETE_WINDOW", self._quitOnClose)
        self._tk.createcommand("exit", self._quitOnClose)
        self._initPuzzle()
        self.reset()

# Public methods

    def getNLevels(self):
        """Returns the number of _levels in the Panex puzzle."""
        return self._nLevels

    def reset(self):
        """Resets the Panex puzzle to its initial configuration."""
        for col in range(3):
            for i in range(1, self._nLevels + 1):
                self._columns[col][i] = None
        for i in reversed(range(1, self._nLevels + 1)):
            piece = self._leftPieces[i]
            self._columns[0][i] = piece
            piece.setColumnAndLevel(0, i)
            piece = self._rightPieces[i]
            self._columns[2][i] = piece
            piece.setColumnAndLevel(2, i)

    def moveSinglePiece(self, start, finish):
        """Moves a piece from start to finish."""
        startIndex = self._findStartIndex(start)
        if startIndex == -1:
            raise ValueError("No disk to move")
        piece = self._columns[start][startIndex]
        finishIndex = self._findFinishIndex(piece, finish)
        if finishIndex == -1:
            raise ValueError("No space for disk")
        self._columns[start][startIndex] = None
        self._columns[finish][finishIndex] = piece
        piece.setColumnAndLevel(finish, finishIndex)
        try:
            self._tk.update()
        except:
            quit()
        time.sleep(SLEEP_TIME)

# Private methods

    def _initPuzzle(self):
        self._createBackground()
        self._createPieces()

    def _createBackground(self):
        frame = GRect(0, 0, self._frameWidth, self._frameHeight)
        frame.setFilled(True)
        frame.setColor(FRAME_COLOR)
        self.add(frame)
        x1 = self._frameWidth / 2
        x0 = x1 - PIECE_WIDTH - COLUMN_SEP
        x2 = x1 + PIECE_WIDTH + COLUMN_SEP
        y0 = TOP_MARGIN + PIECE_HEIGHT / 2
        y1 = self._frameHeight - BOTTOM_MARGIN - PIECE_HEIGHT / 2
        h = CHANNEL_WIDTH / 2
        poly = GPolygon()
        poly.addVertex(x0 - h, y1 + h)
        poly.addVertex(x0 - h, y0 - h)
        poly.addVertex(x2 + h, y0 - h)
        poly.addVertex(x2 + h, y1 + h)
        poly.addVertex(x2 - h, y1 + h)
        poly.addVertex(x2 - h, y0 + h)
        poly.addVertex(x1 + h, y0 + h)
        poly.addVertex(x1 + h, y1 + h)
        poly.addVertex(x1 - h, y1 + h)
        poly.addVertex(x1 - h, y0 + h)
        poly.addVertex(x0 + h, y0 + h)
        poly.addVertex(x0 + h, y1 + h)
        poly.addVertex(x0 - h, y1 + h)
        poly.setFilled(True)
        poly.setColor(CHANNEL_COLOR)
        self.add(poly)

    def _createPieces(self):
        self._leftPieces = [ None ] * (self._nLevels + 1)
        self._rightPieces = [ None ] * (self._nLevels + 1)
        for i in range(1, self._nLevels + 1):
            piece = PanexPiece(LEFT_COLOR, i, self)
            self.add(piece)
            self._leftPieces[i] = piece
            piece = PanexPiece(RIGHT_COLOR, i, self)
            self.add(piece)
            self._rightPieces[i] = piece
        self._columns = [ [ None ] * (self._nLevels + 1) for i in range(3) ]
        
    def _findStartIndex(self, col):
        for i in range(0, self._nLevels + 1):
            if self._columns[col][i] is not None:
                return i
        return -1

    def _findFinishIndex(self, piece, col):
        _level = piece.getLevel()
        for i in range(_level + 1):
            if self._columns[col][i] is not None:
                return i - 1
        return _level

    def _quitOnClose(self):
        try:
            self._tk.destroy()
            quit()
        except:
            pass

# Class: PanexPiece

class PanexPiece(GCompound):

# Constructor

    def __init__(self, color, level, puzzle):
        """Creates a piece with the indicated color and initial level"""
        GCompound.__init__(self)
        self._level = level
        self._puzzle = puzzle
        self.setColor(color)
        frame = GRect(PIECE_WIDTH, PIECE_HEIGHT)
        frame.setFilled(True)
        frame.setColor(PIECE_COLOR)
        self.add(frame, -PIECE_WIDTH / 2, 0)
        poly = GPolygon()
        dw = PIECE_WIDTH / puzzle.getNLevels()
        w0 = (level - 1) * dw
        w1 = level * dw
        poly.addVertex(-w0 / 2, 0)
        poly.addVertex(w0 / 2, 0)
        poly.addVertex(w1 / 2, PIECE_HEIGHT)
        poly.addVertex(-w1 / 2, PIECE_HEIGHT)
        poly.setFilled(True)
        poly.setColor(color)
        self.add(poly)
        border = GRect(PIECE_WIDTH, PIECE_HEIGHT)
        border.setColor(BORDER_COLOR)
        self.add(border, -PIECE_WIDTH / 2, 0)

# Public methods

    def getLevel(self):
        """Returns the initial level of a piece."""
        return self._level

    def setColumnAndLevel(self, column, level):
        """Moves the piece to the specified column and level."""
        try:
            x0 = self._puzzle._frameWidth / 2
            y0 = TOP_MARGIN
            x = x0 + (column - 1) * (PIECE_WIDTH + COLUMN_SEP)
            y = y0 + level * (PIECE_HEIGHT + PIECE_SEP)
            self.setLocation(x, y)
        except:
            pass

# Test method to display a board

def Panex():
    panex = PanexPuzzle(6)
    status = 0
    panex.moveSinglePiece(0,1)
    panex.moveSinglePiece(2,0)

# Startup code

if __name__ == "__main__":
    Panex()