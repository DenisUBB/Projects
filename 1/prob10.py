'''
Created on Mar 3, 2017

@author: Denis
'''

'''
Double every consonant in a string.
 '''


def read_user_command():
    return input("Enter the string : ")

def double_consonant(my_str):
    """
    Doubles every consonant in the string using list slicing
    Input data  : my_str - the string given by the user
    Output data : my_str - the initial string having the consonants doubled
    """ 
    i = 0
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    my_str = list(my_str)
    while i < len(my_str):
        if my_str[i] not in vowels:
            my_str[i + 1:] = my_str[i:]
            i += 1
        i += 1
        
    return "".join(x for x in my_str)
    
    
def main():
    """
    Main function
    """
    my_str = read_user_command()
    my_str = double_consonant(my_str)
    print(my_str)
    
main()
   
            
            
