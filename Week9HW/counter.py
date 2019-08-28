# File: counter.py

"""
This module defines the addCounter function, which adds a counter to an
existing function.  Its purpose is to allow metering or tracing without
editing the original source code.
"""

import inspect

class Counter:
    """This class represents a counter that maintains its local state."""

    def __init__(self, value=0):
        """Initializes the counter to value, which defaults to 0."""
        self.counter = value

    def incr(self, value=1):
        """Increments the counter by value, which defaults to 1."""
        self.counter += value

    def decr(self, value=1):
        """Decrements the counter by value, which defaults to 1."""
        self.counter -= value

    def get(self):
        """Returns the current value of the counter."""
        return self.counter

    def patchFunction(self, fn, patterns, bindings={}):
        """
        Adds a counter to fn which increments the counter at every
        execution of any code fragment in patterns, which is either a
        string representing a complete expression or an array of such
        strings.  This method returns the original function, augmented
        to perform the necessary counts.  A typical usage pattern is

            counter = Counter()
            fib = counter.patchFunction(fib, "fib(n - 1) + fib(n - 2)")
            numberOfAdditions = counter.get()
        """

        if type(patterns) is str:
            patterns = [ patterns ]
        lines = inspect.getsource(fn).splitlines()
        code = lines[0] + "\n"
        for i in range(len(patterns)):
            code += "    def fn_" + str(i) + "(result):\n"
            code += "        _counter.incr()\n"
            code += "        return result\n"
        for line in lines[1:]:
            for i in range(len(patterns)):
                for pattern in patterns:
                    patch = "fn_" + str(i) + "(" + pattern + ")"
                    line = line.replace(pattern, patch)
            code += line + "\n"
        env = bindings.copy()
        env["_counter"] = self
        env[fn.__name__] = fn
        exec(code, env)
        fn = eval(fn.__name__, env)
        return fn
