# Weely Project
generate wordlist easily

# How To Use
you can run it by `python weely.py` and it will use the default arguments

### arguments
`begin`  - set a start point (default is 1)

`until`  - set a limit for passwords (default is True - that mean it will run until you press ctrl+c)

`output` - set output file (default is output.txt)

`alphabets` - set alphabets to use in bruteforcing (default is "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ1234567890!@#*+- " - you can use numbers, symbols, letters)

**example**
this will begin with 11111, end with 90000 passwords, will use in bruteforcing 123456789 and the output file will be output.txt

`python weely.py begin=5 until=90000 alphabets=1234567890 output=output.txt`


for help type `python weely.py --help`


# Weely Modules
[gmail.py](gmail.py) - Bruteforce gmail accounts (not for evil uses)

# Performance
generated 9211 passwords within 1.128 seconds on medium intel processor

# Contributing
are pull requests are welcomed.

just build you own weely like module, or just improve
an existing one.

# License
released under **Gnu General Public License 3**
