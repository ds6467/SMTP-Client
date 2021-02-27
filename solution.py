from socket import *
import sys


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My Message"
    endmsg = "\r\n.\r\n"
    mail_command = ('MAIL FROM: <ds6467@nyu.edu>\r\n')
    rcpt_command = ('RCPT TO: <donald.shkembi@hotmail.com>\r\n')
    data = "DATA \r\n"
    subject = "Subject: testing my smtp client code \r\n\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    mailserver = '127.0.0.1'
    port = 1025

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()
    #print(recv)
    if (recv[:3] != '250') and (recv[:3] != '354'):
        # Send HELO command and print server response.
        heloCommand = 'HELO Alice\r\n'
        clientSocket.send(heloCommand.encode())
        recv = clientSocket.recv(1024).decode()

        # Send MAIL FROM command and print server response.
        # from who the message will appear
        clientSocket.send(mail_command.encode())
        recv = clientSocket.recv(1024).decode()

        # Send RCPT TO command and print server response.

        # Recepient
        clientSocket.send(rcpt_command.encode())
        recv = clientSocket.recv(1024).decode()

        # Send DATA command and print server response.

        clientSocket.send(data.encode())
        recv = clientSocket.recv(1024).decode()

        # Send message data.

        clientSocket.send(subject.encode())
        clientSocket.send(msg.encode())
        clientSocket.send(endmsg.encode())

        # Message ends with a single period.

        recv_msg = clientSocket.recv(1024).decode()
        # print('220 reply not received from server.')
        quitcommand = ('QUIT\r\n')
        clientSocket.send(quitcommand.encode())
        recv = clientSocket.recv(1024).decode()

        clientSocket.close()

    else:
        sys.exit()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
