'''
Created on Mar 3, 2017

@author: Denis
'''
import random

'''
Generate 100 random integers from the range 1e15..1e16; check them for primality.
'''


def is_prime(num):
    '''
    Fermat's primality test
    Input  : num - the number to be tested
    Output : True - if the number is prime
             False - otherwise
    '''
    if num == 2:
        return True
    if not num & 1:  # even number
        return False
    return pow(2, num - 1, num) == 1


def test_for_primality():
    for i in range(101):
        x = random.randint(1e50, 1e51)
        print(i, ": ", x, is_prime(x))

test_for_primality()
