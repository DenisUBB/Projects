'''
Created on Mar 3, 2017

@author: Denis
'''

'''
Check the minimum security requirements of a password 
(at least one digit, one symbol, one lower, one upper, length 12..14). 
'''


def read_user_command():
    return input("Enter the password : ")


def check_pass(passw):
    '''
    Checks the strength of a password
    Input data  : passw - the given password
    Output data : True - if the password is good enough
                  False - otherwise
    '''
    l = []
    l.append(any(c.isdigit() for c in passw))
    l.append(any(not c.isdigit() and not c.isalpha()
                 for c in passw))  # special character
    l.append(any(c.isupper() for c in passw))
    l.append(any(c.islower() for c in passw))
    l.append(len(passw) >= 12 and len(passw) <= 14)
    for x in l:
        if x == False:
            return False
    return True


def main():
    '''
    Main function
    '''
    while(True):
        passw = read_user_command()
        if check_pass(passw) == False:
            print("Invalid password")
        else:
            return

main()
