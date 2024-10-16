import socket
import sys


#socket creation for connection:
def socket_create():
    try:
        global port
        global host
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg: 
        print("socket error: " + str(msg))


#binding socket

def socket_bind():
    try:
        global port
        global host
        global s
        print("")
        print("Binding socket to port: " + str(port))
        s.bind((host, port))
        s.listen(7)
    except socket.error as msg:
        print("Binding error: " + str(msg) + "\n" + "Trying again...")
        socket_bind()


#create connection with client: 
def socket_accept():
    conn, addr = s.accept()


        
    


