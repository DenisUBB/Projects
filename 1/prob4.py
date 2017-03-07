'''
Created on Mar 3, 2017

@author: Denis
'''

'''
Create a dictionary containing a mapping from n to the last four non-zero digits of n! for n = k..k+100, 100 <= k <= 1000. 
'''


def read():
    return int(input("n = "))


def fact(n):
    '''
    Factorial function
    Input  : n - an integer
    Output : n!
    '''
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)


def mapping(n):
    d = {}
    for i in range(n, fact(n) % 10000 + 1):
        d[i] = fact(n)
    return d


def main():
    '''
    Main function
    '''
    n = read()
    d = mapping(n)
    for key, elem in d.items():
        print(key, elem)

main()
