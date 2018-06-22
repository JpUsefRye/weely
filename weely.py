# Author: JpUsefRye
# GitHub: https://github.com/JpUsefRye/weely
# License: GPL3
import time
import sys
import itertools
from parser import Parser

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

def bruteforce(alphabets: str,
               output: str, begin: int,
               until: int, api=False,
               func=None) -> None:

    # Start Counting
    start = time.time()

    # wwa stands for 'where we are'
    wwa = 0

    if not isinstance(api, bool):
        raise ValueError("(api) parameter is not instance of bool")

    if api:
        if func == None:
            print("Warning: you did not specify a function, ignoring...")

    try:
        for a in range(begin, len(alphabets) + 1):
            if not api:
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
            else:
                func(start=start,
                     wwa=wwa, alphabets=alphabets,
                     a=a, b=b)
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
