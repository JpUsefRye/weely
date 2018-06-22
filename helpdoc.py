import sys
import time

def header() -> None:
    print("Author: @JpUsefRye")
    print("Github link: https://github.com/JpUsefRye/weely")

def arguments() -> None:
    print("begin        set a start point")
    print("alphabets    set alphabets to use in generating wordlist")
    print("output       set output file")
    print("--help       show this message")

def weely_usage() -> None:
    header()
    print("Info: Fastest Wordlist generator you will ever see")
    print(f"USAGE: {sys.argv[0]} [...]")
    arguments()

def gmail_usage() -> None:
    header()
    print("Weely Gmail Module")
    print("USAGE: {sys.argv[0]} email=EMAIL [...]")

def weely_goodbye(start: float, wwa: int) -> None:
    print(f"It took {round(time.time()-start,3)} seconds")
    print(f"This file contains now {wwa} passwords")
    sys.exit(0)

def gmail_goodbye(start: float, wwa: int) -> None:
    print(f"It took {round(time.time()-start,3)} seconds")
    print(f"Password tried in this operation: {wwa}")
    sys.exit(0)
