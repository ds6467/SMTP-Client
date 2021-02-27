from socket import *
import sys


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My Message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    mailserver = '127.0.0.1'
    port = 1025

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()
    # print(recv)
    if recv[:3] != '220':
       clientSocket.close()
       sys.exit()


    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != '250':
       clientSocket.close()
       sys.exit()



    # Send MAIL FROM command and print server response.

    x = 0
    while True:
       # input Sender email
       while True:
          from_input = raw_input('From: ')
          clientSocket.send('MAIL FROM: <' + from_input + '>')
          okFrom = clientSocket.recv(1024)
          if okFrom[:3] != "250":
             print('Please enter a valid email address.')
             continue
          else:
             break


      while True:
         if x is 1:
            clientSocket.send('RCPT TO: <' + rec + '>')
            okTo = clientSocket.recv(1024)

         if x is 0:
            break



    data = "DATA \r\n"
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()
    if recv4[:3] != '354':  # if the data is not received
       sys.exit()

    write_from = ('From: ' + from_input)
    clientSocket.send(write_from.encode())
    clientSocket.recv(1024)

    write_To = ('To: ' + to)
    clientSocket.send(write_To)
    clientSocket.recv(1024)

    read_Subject = raw_input('Subject: ')
    clientSocket.send('Subject: ' + read_Subject + '\n')
    clientSocket.recv(1024)

    sys.stdout.write('Message: ')

    # read email msg until "."
    while True:
       read_Data = raw_input()
       if read_Data == '':
          read_Data = '\r'
       clientSocket.sendall(read_Data)
       okEnd = clientSocket.recv(1024)
       if okEnd[:3] == '250':
          clientSocket.send('QUIT')
          quit_Msg = clientSocket.recv(1024)
          if quit_Msg[:3] != '221':
             print
             'There was an error. Quitting.'
             sys.exit()
          else:
             clientSocket.close()
             exit()
       else:
          continue





if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
