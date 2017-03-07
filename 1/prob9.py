'''
Created on Mar 3, 2017

@author: Denis
'''

'''
Write max() and sum() functions for two-dimensional matrices.
'''


def read_matrix():
    '''
    Reads a matrix by n rows and m columns(no validaton made)
    Input data  : -
    Output data : the matrix read by the user
    '''
    n = int(input("n="))
    m = int(input("m="))
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            print("a[{}][{}] = ".format(i, j))
            matrix[i].append(int(input()))
    return matrix


def sum1(matrix):
    '''
    Does the sum of all the elements of a 2d array
    Input data  : matrix - our current matrix of integers
    Output data : the sum of the elements within current matrix
    '''
    return sum(map(sum, matrix))


def max1(matrix):
    '''
    Finds the maximum element in a 2d array
    Input data  : matrix - our current matrix of integers
    Output data : max elem
    '''
    return max(map(max, matrix))


def main():
    '''
    Main function
    '''
    matrix = read_matrix()
    print('The sum of the elements ', sum1(matrix))
    print('The max of the elements', max1(matrix))


main()
