#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
host = "192.168.0.16"
serverPort = 6789
serverSocket.bind((host, serverPort))
serverSocket.listen(5)
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(4096)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.readlines()
    #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\nContent-type:text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        # Fill in start
        connectionSocket.send("HTTP/ 1.1 404 Not Found\r\n".encode())
        connectionSocket.send("Content-Type: text/html\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
    #Send response message for file not found
    #Fill in start 
    #Fill in end
    #Close client socket
    #Fill in start
    #Fill in end
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data 