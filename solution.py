from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"  
    endmsg = "\r\n.\r\n"

    # Choose a mail server
    # port = 25
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # mailserver = 'smtp.nyu.edu'
    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    # Fill in end

    recv = clientSocket.recv(1024).decode()

    # Send HELO command and print server response.
    heloCommand = 'HELO Donald\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailCommand = 'MAIL FROM:<ds6467@nyu.edu>\r\n'
    clientSocket.send(mailCommand.encode())
    recv2 = clientSocket.recv(1024).decode()


    # Send RCPT TO command and print server response.
    # Fill in start
    rcptCommand = 'RCPT TO:<ds6467@nyu.edu>\r\n'
    clientSocket.send(rcptCommand.encode())
    recv3 = clientSocket.recv(1024).decode()

    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()


    # Send message data.

    # Fill in start
    clientSocket.send(msg.encode())

    # Fill in end

    # Message ends with a single period.
    # Fill in start

    clientSocket.send(endmsg.encode())

    recv1 = clientSocket.recv(1024).decode()

    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv5 = clientSocket.recv(1024).decode()



if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
