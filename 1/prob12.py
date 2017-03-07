'''
Created on Mar 3, 2017

@author: Denis
'''

'''
Compute the square root of a number by bisection.
'''


def read():
    number = float(
        input("Enter the number to calculate the square root for : "))
    return number


def bisection(nr):
    '''
    Calculates the square root of nr by bisection
    Input data  : nr - an floating number for which we need to calculate the square root
    Output data : 
    '''
    if nr < 0:
        print("According to math is not possible")
    else:
        low = float(0)
        high = float(nr)
        mid = (low + high) / 2
        c = 0
        while c != 1:
            if mid * mid == nr:
                print("Square root is: ", mid)
                c = 1
            else:
                if mid * mid > nr:
                    high = mid
                    mid = (low + high) / 2
                else:
                    low = mid
                    mid = (low + high) / 2


def main():
    number = read()
    bisection(number)

main()
