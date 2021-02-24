
# import socket module
from socket import *
import sys  # In order to terminate the program


def webServer(port=8080):

    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverHost = '127.0.0.1'
    serverPort = 8080

    # Prepare a sever socket
    serverSocket.bind((serverHost, serverPort))
    serverSocket.listen(5)
    print('The server is ready to receive')

    # Fill in end

    while True:
        # Establish the connection
        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()  # Fill in end
        try:
            message = connectionSocket.recv(4096)
            filename = message.split()[1]
            f = open(filename[1:])
            outputdata = f.readlines()

            # print(outputdata)

            # Send one HTTP header line into socket
            connectionSocket.send(("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n").encode())
            connectionSocket.send(("\r\n").encode())
            # Fill in start

            # Fill in end

            # Send the content of the requested file to the client
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()
        except IOError:
            # Send response message for file not found (404)
            connectionSocket.send(("HTTP/ 1.1 404 Not Found\r\n").encode())
            connectionSocket.send(("Content-Type: text/html\r\n").encode())
            connectionSocket.send(("\r\n").encode())
            connectionSocket.send(("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n").encode())
            # Fill in start

            # Fill in end

            # Close client socket
            # Fill in start

            # Fill in end

    serverSocket.close()
    sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(8080)