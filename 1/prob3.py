'''
Created on Mar 3, 2017

@author: Denis
'''

'''
Find two coprime integers in the range 1e50..1e51. 
'''

import random


def gcd(x, y):
    '''
    GCD using Euclidean algorithm
    Input  : x,y - 2 integers
    Output : gcd(x, y)
    '''
    c = 1
    while c:
        c = x % y
        x = y
        y = c
    return x


def coprime():
    '''
    Finds 2 coprime numbers between [1e50, 1e51]
    '''
    while True:
        x = random.randint(1e50, 1e51)
        y = random.randint(1e50, 1e51)
        if gcd(x, y) == 1:
            print(x, y)
            break
coprime()