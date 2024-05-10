import socket

SERVER_IP = 'localhost'
SERVER_PORT = 12345
FORMAT = 'utf-8'

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((SERVER_IP,SERVER_PORT))

receivedFileData = clientSocket.recv(1024)

with open("receivedFile.txt", 'wb') as file:
    file.write(receivedFileData)

clientSocket.close()