'''
Created on Mar 7, 2017

@author: Denis
'''
import random
import re

#######Enter the string here#######
s = '''a
    ab'''
###################################


def create_dict():
    """
    Choses random numbers between [1000 - 9999] and assings to each letter from the alphabet
    one of those numbers
    """
    d = {}
    for i in range(ord('a'), ord('z') + 1):
        gotRand = False
        while not gotRand:
            nr = random.randint(1000, 9999)
            if nr not in d.values():
                d[chr(i)] = nr
                gotRand = True
    return d


def multiline_encode(s):
    """
    Encodes a multiline string
    We use regex to eliminate extra spaces added by python
    """
    d = create_dict()
    s = re.sub(r'(\n)\s*([a-zA-Z])', r'\1\2', s)
    s = list(s)  # convert the string to a list

    for i in range(len(s)):
        if s[i] in d:
            s[i] = str(d[s[i]])
    c = s
    s = ''.join(s)   # convert back the list to str
    return d, s, c


def multiline_decode(s, d):
    """
    Decodes a multiline string
    """
    d = {v: k for k, v in d.items()}
    for i in range(len(s)):
        if s[i].isdigit():
            s[i] = int(s[i])
            s[i] = d[s[i]]
    return ''.join(s)


def main(s):
    """
    Principal function
    """
    d, s, c = multiline_encode(s)
    print("Encoded multiline string:")
    print(s)
    s_decoded = multiline_decode(c, d)
    print("Decoded multiline string:")
    print(s_decoded)

main(s)
