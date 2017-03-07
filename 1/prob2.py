'''
Created on Mar 3, 2017

@author: Denis
'''

'''
Print all primes between 100000000000 and 100000010000 (inclusive) separated by semicolons (;).
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


def next_prime(num):
    '''
    Gets the next prime number using the fact that the prime numbers
    are only odd numbers(excepting 2), so we go from 2 in 2
    Input  : num - finding the next number for num
    Output : next prime number
    '''
    if num & 1 == 1:
        num += 2
    else:
        num += 1
    while True:
        if is_prime(num):
            break
        num += 2
    return num


def all_primes():
    i = 100000000000
    while i <= 100000010000:
        i = next_prime(i)
        print(i)

all_primes()
