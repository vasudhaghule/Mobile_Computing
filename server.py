import socket

SERVER_IP = 'localhost'
SERVER_PORT = 12345
FORMAT = 'utf-8'

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((SERVER_IP,SERVER_PORT))

serverSocket.listen(1)
clientSocket, clientAddress = serverSocket.accept()

with open('example.txt', 'rb') as file:
    fileData = file.read()
    clientSocket.sendall(fileData)

serverSocket.close()
