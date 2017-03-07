'''
Created on Mar 5, 2017

@author: Denis
'''
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


def censor_email():
    """
    Censors the email addresses by the given pattern
    The emails are found in input_file.txt and the consored ones will be stored
    in output_file.txt
    """
    input = 'input_file.txt'
    output = 'output_file.txt'
    with open(output, 'w') as f:
        for email in find_emails(read_file(input)):
            email = re.sub(r'(\w)[\w.-]+([a-zA-Z\d]@)',  r'\1***\2', email)
            email = re.sub(r'(@)[a-zA-z]+(\.)', r'\1***\2', email)
            f.write(email + '\n')


censor_email()
