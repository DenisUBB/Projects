'''
Created on Mar 3, 2017

@author: Denis
'''

'''
Count uppercase and lowercase letters in a text. 
'''


def read_user_command():
    return input("Enter the string : ")


def upperc_lowerc_letters(my_str):
    '''
    Counts the number of uppercase and lowercase characters
    Input data  : my_str - the string where we'll be counting the ascii_letters
    Output data : lc - lowercase characters in our string
                  uc - uppercase characters in our string
    '''
    lc = sum(1 for c in my_str if c.islower())
    uc = sum(1 for c in my_str if c.isupper())
    return lc, uc


def main():
    '''
    Principal function
    '''
    my_str = read_user_command()
    lowerC, upperC = upperc_lowerc_letters(my_str)
    print("Nr. of lowercase characters: ", lowerC)
    print("Nr. of uppercase characters: ", upperC)

main()
