# Author: JpUsefRye
# GitHub: https://github.com/JpUsefRye/weely
# License: GPL3
import time
import os
import sys
import itertools


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

def usage() -> None:
    print("Author: @JpUsefRye")
    print("Github link: https://github.com/JpUsefRye/weely")
    print("Info: Fastest Wordlist generator you will ever see")
    print(f"USAGE: {sys.argv[0]} [argument 1] [argument 2]")
    print("Arguments (arguments are optional):")
    print("begin        set a start point")
    print("alphabets    set alphabets to use in generating wordlist")
    print("output       set output file")
    print("--help       show this message")

def goodbye(start: float, wwa: int) -> None:
        print("It took {0} seconds".format(round(time.time() - start, 3)))
        print("This file contains now {0} passwords".format(wwa))
        sys.exit(0)

def bruteforce(alphabets: str, output: str, begin: int, until: int) -> None:

    # Start Counting
    start = time.time()

    # wwa stands for 'where we are'
    wwa = 0

    try:
        for a in range(begin, len(alphabets) + 1):
            for b in itertools.product(alphabets, repeat=a):
                k = "".join(b)
                print("writing:", k)
                with open(output, 'a') as op:
                    op.write(k+'\n')
                wwa+=1

                if until != True:
                    if wwa == until:
                        goodbye(start, wwa)
                        return
    except KeyboardInterrupt as e:
        goodbye(start, wwa)

def main() -> None:
    parser = Parser()
    if not isinstance(parser.get_alphabets(), str):
        raise ValueError("alphabets must be a string (e.g alphabets=abcd1234)")
    if not isinstance(parser.get_output(), str):
        raise ValueError("output must be a string: (e.g output=output.txt)")
    if not isinstance(parser.get_until(), int):
        if isinstance(parser.get_until(), bool):
            pass
        raise ValueError("until must be an integer (e.g until=9)")
    if not isinstance(parser.get_begin(), int):
        raise ValueError("begin must be an integer (e.g begin=5)")

    bruteforce(parser.get_alphabets(),
               parser.get_output(),
               parser.get_begin(),
               parser.get_until())

if __name__ == '__main__':
    main()
