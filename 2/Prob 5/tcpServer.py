"Made on python 2.7.13"
"Vieriu Denis - Gabriel"
import socket
import random
import hashlib
import zlib


def random4():
    """
    Returns a 4 byte number chosen randomly
    """
    return str(random.randint(0, 1<<32 - 1))

def random8():
    """
    Returns a 8 byte number chosen randomly
    """
    return str(random.randint(0, 1<<64 - 1))


def is_prime(n):
    """
    Checks if a number is prime
    Input data  : n - the number to be checked
    Output data : the number is/ is not prime
    """
    if n < 2:
        return "The number {} is not prime".format(n)
    elif n > 2 and n % 2 == 0:
        return "The number {} is not prime".format(n)
    for i in range(3, n, 2):
        if i * i > n:
            break
        elif n%i == 0:
            return "The number {} is not prime".format(n)
    return "The number {} is prime".format(n)

        
def ROTn(text, key):
    """
    Ceasar_cipher function, key will be the root
    Input data  : text - given text
                  key  - the rot
    Output data : encrypted string
    """
    cipher = ''
    alphabet = ''.join(chr(i) for i in range(ord('a'), ord('z') + 1))
    for i in text:
        if i in alphabet:
            cipher += alphabet[(alphabet.index(i) + key) % (len(alphabet))] 
    return cipher


def Main():
    """
    Starting the server;
    Main loop is found here;
    Sends to the client the asked information 
    """
    host = "127.0.0.1"
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1)
    c, addr = s.accept()

    selected_cond_1 = selected_cond_2 = selected_cond_3 = selected_cond_4 = selected_cond_5 = False
    
    print "Connection from: " + str(addr)
    while True:
        data = c.recv(1024)
        send_this = "Nothing to be sent"
        if not data:
            break
        print "from connected user: " + str(data)
        try:
            if data == "1" or selected_cond_1:
                if not selected_cond_1:
                    send_this = "4 byte or 8 byte number? [4\8]"
                    selected_cond_1 = True  # remember that we have pressed the 1 keyboard for the next command [4\8] byte number
                elif data == "4":
                    send_this = random4()   # 4 byte random number
                    selected_cond_1 = False
                elif data == "8":
                    send_this = random8()   # 8 byte random number
                    selected_cond_1 = False
                else:
                    send_this = "Wrong command!"
                    selected_cond_1 = False
            elif data == "2" or selected_cond_2:
                if not selected_cond_2:
                    send_this = "Enter the number to be checked: "
                    selected_cond_2 = True
                else:
                    data = int(data)
                    selected_cond_2 = False
                    send_this = is_prime(data)
            elif data == "3" or selected_cond_3:
                if not selected_cond_3:
                    send_this = "Enter the data to be hashed:"
                    selected_cond_3 = True
                else:
                    send_this = hashlib.sha224(data).hexdigest()
                    selected_cond_3 = False
            elif data == "4" or selected_cond_4:
                if not selected_cond_4:
                    send_this = "encrypt\decrypt data"
                    selected_cond_4 = True
                else:
                    data = data.split()
                    data1 = data[0]
                    data2 = ''.join(data[1:])
                    if data1 == "encrypt":
                        send_this = ROTn(data2, 13)
                    elif data1 == "decrypt":
                        send_this = ROTn(data2, 13)
                    else:
                        send_this =  "Invalid"
                    selected_cond_4 = False
            elif data == "5" or selected_cond_5:
                if not selected_cond_5:
                    send_this = "Enter the data:"
                    selected_cond_5 = True
                else:
                    compressed_data = zlib.compress(data)
                    decompressed_data = zlib.decompress(compressed_data)
                    send_this  = "Compressed data is : " + str(compressed_data) + "\n"
                    send_this += "Decompressed data is: " + str(decompressed_data) + "\n"
                    selected_cond_5 = False
            elif data == "6":
                send_this = "matrix"
        except:
            send_this = "Error"
        c.send(send_this)
    c.close()
    
if __name__ == "__main__":
    Main()
