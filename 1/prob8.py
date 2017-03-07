'''
Created on Mar 3, 2017

@author: Denis
'''

'''
Generate 10 random passwords meeting the requirements.
'''

import random


def generatePw():
    '''
    Generates 10 passwords meeting the requirments
    Data : lc - list of all lowercase letters
           uc - list of all uppercase letters
           digit - list of all digits from 0 to 9
           symbol - list of some symbols
           length - chosen randomly between 12 and 14
           l - a list where we store  all the list mentionated above
               from where we'll be chosing randomly characters and insert
               them in newPw(after we meet the minimum requirments)
    '''
    lc = ''.join(chr(i) for i in range(ord('a'), ord('z') + 1))
    uc = ''.join(chr(i) for i in range(ord('A'), ord('Z') + 1))
    digit = ''.join(chr(i) for i in range(ord('0'), ord('9') + 1))
    symbol = "~`!@#$%^&*()_-+={}[]:>;',</?*-+"
    for i in range(11):
        l = []
        newPw = []
        l.extend([lc, uc, digit, symbol])
        newPw.append(random.choice(lc))
        newPw.append(random.choice(uc))
        newPw.append(random.choice(digit))
        newPw.append(random.choice(symbol))
        lenght = random.randint(12, 14)
        while len(newPw) != lenght:
            newPw.append(random.choice(l[random.randint(0, 3)]))
        print(''.join(x for x in newPw))


generatePw()
