# File: consoletest.py

"""
This module implements an interactive test harness in which the
user enters a sequence of commands on the console.
"""

# Code to ensure that imported modules can come from the current directory

import os
import sys
sys.path.insert(0, os.getcwd())

from tokenscanner import TokenScanner
import types

# The ConsoleTest class is a base class for writing convenient interactive
# tests that read and execute commands from the console.  To define a new
# command xxx, all that the subclass needs to do is define a method that
# fits the following pattern:
#
#     def xxxCommand(self, scanner):
#         """Help text for the command"""
#         Code to implement the command

class ConsoleTest:

    def run(self):
        """Runs the interactive test program."""
        while True:
            line = input(self.getPrompt())
            self.execute(line)

    def execute(self, line):
        scanner = self.createScanner()
        scanner.setInput(line)
        token = scanner.nextToken()
        if token != "":
            cmd = self.lookup(token)
            if cmd is None:
                scanner.saveToken(token)
                self.undefinedCommandHook(scanner)
            else:
                cmd(scanner)

    def lookup(self, cmd):
        fn = getattr(self, cmd + "Command", None)
        if type(fn) != types.MethodType:
            return None
        return fn

# Builtin commands

    def quitCommand(self, scanner):
        """quit -- Quits the program"""
        sys.exit()

    def helpCommand(self, scanner):
        """help -- Prints this help text"""
        commands = [ ]
        for cmd in dir(self):
            if cmd.endswith("Command"):
                fn = getattr(self, cmd, None)
                if type(fn) == types.MethodType:
                    commands.append(fn)
        maxDoc = 0
        for fn in commands:
            docstr = fn.__doc__
            if docstr is not None:
                dash = docstr.find(" -- ")
                if dash != -1:
                    maxDoc = max(maxDoc, dash)
        for fn in commands:
            docstr = fn.__doc__
            if docstr is None:
                print(fn.__name__[:-len("Command")])
            else:
                dash = docstr.find(" -- ")
                if dash == -1:
                    print(docstr)
                else:
                    head = docstr[:dash]
                    tail = docstr[dash:]
                    print(head.ljust(maxDoc) + tail)

    def scriptCommand(self, scanner):
        """script "file" -- Reads a script from the file"""
        filename = self.scanFilename(scanner)
        if "." not in filename:
            filename += ".txt"
        with open(filename) as f:
            for line in f.read().splitlines():
                print(self.getScriptPrompt() + line)
                self.execute(line)

    def scanFilename(self, scanner):
        filename = ""
        while (scanner.hasMoreTokens()):
            filename += scanner.nextToken()
        return filename

    def nextInt(self, scanner):
        sign = 1
        token = scanner.nextToken()
        if token == "-":
            sign = -1
            token = scanner.nextToken()
        return sign * int(token)

    def nextFloat(self, scanner):
        sign = 1
        token = scanner.nextToken()
        if token == "-":
            sign = -1
            token = scanner.nextToken()
        return sign * float(token)

# Methods available for clients to override

    def createScanner(self):
        """Creates the scanner used in this test program."""
        scanner = TokenScanner()
        scanner.ignoreWhitespace()
        scanner.scanNumbers()
        scanner.scanStrings()
        return scanner

    def getPrompt(self):
        return "-> "

    def getScriptPrompt(self):
        return "+> "

    def undefinedCommandHook(self, scanner):
        print("Undefined command: " + scanner.nextToken())
