#Vieriu Denis - Gabriel
import socket


def get_menu():
    """
    Returns a menu containing all the instructions
    """
    msg  = 'Server started!\n\r'
    msg += 'Avalaible commands:\n\r'
    msg += '\t1 - random 4 byte or 8 byte number\n\r'
    msg += '\t2 - checking if a given number is is_prime\n\r'
    msg += '\t3 - hashing of data\n\r'
    msg += '\t4 - encryption and decryption of binary data (any encryption)\n\r'
    msg += '\t5 - compression and decompression of binary data\n\r'
    msg += '\t6 - matrix multiplication on lists\n\r'
    return msg


def read_matrix():
    """
    Reads a matrix by n rows, m columns and returns it
    """
    n = int(raw_input("Enter the number of lines for first matrix"))
    m = int(raw_input("Enter the number of columns for first matrix"))
    matrix = []
    for i in range(0, n):
        matrix.append([])
        for j in range(0, m):
            print "a[{}][{}] = ".format(i, j) 
            matrix[i].append(int(raw_input()))
    return n, m, matrix


def matrix_mul(X, Y, Z):
    """
    Does matrix multiplications on X and Y, and stores the result in Z;
    returns Z
    """
    for i in range(len(X)):
        # iterating over rows of X
        for j in range(len(Y[0])):
            # iterating over columns of Y
            for k in range(len(Y)):
                # iteraing over rows of Y
                Z[i][j] += X[i][k] * Y[k][j]
    return Z


def destination(n, m):
    """
    Creates a destination matrix for the matrix multiplications and returns it
    """
    dest = []
    for i in range(n):
        dest.append([])
        for j in range(m):
            dest[i].append(0)
    return n, m, dest

            
def Main():
    """
    Starts the client
    Allows to send data the the server and receive information
    """
    host = "127.0.0.1"
    port = 5000

    s = socket.socket()
    s.connect((host, port))

    main_menu = get_menu()
    print main_menu

    message = raw_input("->")
    while message != 'q':
        s.send(message)
        data = s.recv(1024)
        print "Received from server: " + str(data)
        if data == "matrix":
            n1, m1, matrix1 = read_matrix()
            n2, m2, matrix2 = read_matrix()
            n, m, destMatrix = destination(n1, m2)
            print(str(matrix_mul(matrix1, matrix2, destMatrix)))
            

        message = raw_input("->")
    s.close()


if __name__ == "__main__":
    Main()
