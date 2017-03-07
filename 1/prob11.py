'''
Created on Mar 3, 2017

@author: Denis
'''

'''
Create a ROT-3 (Caesar cipher) function. 
'''

def read_user_command():
    return input("Enter the text: ")

def caesar_cipher(text, key):
    '''
    Ceasar_cipher function, key will be the root
    Input data  : text - given text
                  key  - the rot
    Output data : encrypted string
    '''
    cipher = ''
    alphabet = ''.join(chr(i) for i in range(ord('a'), ord('z') + 1))
    for i in text:
        if i in alphabet:
            cipher += alphabet[(alphabet.index(i) + key) % (len(alphabet))] 
    return cipher

def main():
    '''
    Principal function
    '''
    text = read_user_command()
    print(caesar_cipher(text, 3))
    
main()