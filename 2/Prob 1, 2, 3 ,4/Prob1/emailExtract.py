'''
Created on Mar 5, 2017

@author: Denis
'''

from optparse import OptionParser
import os.path
import re


reg = re.compile(("[\w\-\.]+@[\w\-\.]+"))  # format of an email address


def read_file(filename):
    """
    Returns the content of the file as a string
    Input data  : filename - the file to read
    Output data : content of the file
    """
    with open(filename, 'r') as f:
        return f.read().lower()     # email addresses are case insensitive


def find_emails(string):
    """
    Searches for emails in our string from the opened file
    Input data  : string - all email adresses
    Output data : an iterator of matched emails in the string
    """
    return (email for email in re.findall(reg, string))


if __name__ == '__main__':
    parser = OptionParser()  # needed to parse the arguments
    options, args = parser.parse_args()

    if not args:
        exit(1)   # cannot use return since we're not in any function

    for arg in args:
        if os.path.isfile(arg):
            for email in find_emails(read_file(arg)):
                print(email)
        else:
            print('"{}" is not a file.'.format(arg))
