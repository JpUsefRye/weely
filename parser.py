import os
import sys

#: command line argument parser
#: i just do not want to use external libs
class Parser(object):
        #: a bit confusing
        #
        #
        # the user will input in arguments:
        # >>> python weely.py begin=7 alphabets=0123456789 output=output.txt until=8
        # this will parse the arguments like that
        #
        # begin=7
        # alphabets=0123456789
        # ...
        #
        # then split the '=' sign
        # will result something like that
        # ['begin', '7']
        # we will get element index 1
        #
    def __init__(self) -> None:
        arguments = sys.argv
        self.begin = 1
        self.alphabets = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890!@#*+- "
        self.output = 'output.txt'
        self.until = True

        for argument in arguments:
            if 'begin' in argument:
                self.begin = arguments[arguments.index(argument)].split('=')[1]
            if 'alphabets' in argument:
                self.alphabets = arguments[arguments.index(argument)].split('=')[1]
            if 'output' in argument:
                self.output = arguments[arguments.index(argument)].split('=')[1]
            if 'until' in argument:
                self.until = arguments[arguments.index(argument)].split('=')[1]
            if '--help' in argument:
                usage()
                sys.exit(0)


    def get_begin(self) -> int:
        return int(self.begin)

    def get_until(self) -> int:
        return int(self.until)

    def get_alphabets(self) -> str:
        return self.alphabets

    def get_output(self) -> str:
        return self.output
