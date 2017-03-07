'''
Created on Mar 3, 2017

@author: Denis
'''


def matrix_mul():
    '''
    Does a matrix multiplication between 2 matrix
    '''

    X = [[3, -5, 7],
         [-2, 4, 6]]

    Y = [[12, -7],
         [3, 4],
         [11, 8]]

    Z = [[0, 0],
         [0, 0]]

    for i in range(len(X)):
        # iterating over rows of X
        for j in range(len(Y[0])):
            # iterating over columns of Y
            for k in range(len(Y)):
                # iteraing over rows of Y
                Z[i][j] += X[i][k] * Y[k][j]

    for r in Z:
        print(r)

matrix_mul()
