# Author: JpUsefRye
# GitHub: https://github.com/JpUsefRye/weely
# License: GPL3
import time
import sys
import itertools
from parser import Parser
from helpdoc import weely_goodbye

def bruteforce(alphabets: str,
               output: str, begin: int,
               until: int, api=False,
               func=None, func_farg=None) -> None:

    # Start Counting
    start = time.time()

    # wwa stands for 'where we are'
    wwa = 0

    if not isinstance(api, bool):
        raise ValueError("(api) parameter is not instance of bool")

    if api:
        if func == None:
            print("Warning: you did not specify a function, ignoring...")
            sys.exit(1)

    try:
        for a in range(begin, len(alphabets) + 1):
            for b in itertools.product(alphabets, repeat=a):
                k = "".join(b)
                if not api:
                    print("writing:", k)
                    with open(output, 'a') as op:
                        op.write(k+'\n')
                    wwa+=1

                    if until != True:
                        if wwa == until:
                            goodbye(start, wwa)
                else:
                    if func_farg != None:
                        func(start, waa,
                             func_farg, k)
                    else:
                        sys.exit(0)
    except KeyboardInterrupt as e:
        weely_goodbye(start, wwa)

def main() -> None:
    parser = Parser()

    bruteforce(parser.get_alphabets(),
               parser.get_output(),
               parser.get_begin(),
               parser.get_until())

if __name__ == '__main__':
    main()
