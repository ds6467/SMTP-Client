from socket import *



def smtp_client(port=1025, mailserver='127.0.0.1'):
   msg = "\r\n My message"
   endmsg = "\r\n.\r\n"



   # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
   mailserver = ("smtp.nyu.edu", 25)
   # Create socket called clientSocket and establish a TCP connection with mailserver and port
   clientSocket = socket(AF_INET, SOCK_STREAM)
   clientSocket.connect(mailserver)

   recv = clientSocket.recv(1024).decode()
   print(recv)
   if recv[:3] != '220':
       #print('220 reply not received from server.')

   # Send HELO command and print server response.
   heloCommand = 'HELO Alice\r\n'
   clientSocket.send(heloCommand.encode())
   recv1 = clientSocket.recv(1024).decode()
   print(recv1)
   if recv1[:3] != '250':
       #print('250 reply not received from server.')

   # Send MAIL FROM command and print server response.
   mail_command = ('MAIL FROM:<ds6467@nyu.edu> \r\n') # from who the message will appear
   clientSocket.send(mail_command.encode())
   recv1 = clientSocket.recv(1024).decode()
   if recv1[:3] != '250': #if the data is not received
      #print('250 reply not received from server.')

   # Send RCPT TO command and print server response.
   rcpt_command = ('RCPT TO:<shkembi.donald@gmail.com> \r\n') # Recepient
   clientSocket.send(rcpt_command.encode())
   recv1 = clientSocket.recv(1024).decode()
   if recv1[:3] != '250':  # if the data is not received
      #print('250 reply not received from server.')


   # Send DATA command and print server response.
   data = 'DATA \r\n'
   clientSocket.send(data.encode())
   recv1 = clientSocket.recv(1024).decode()
   if recv1[:3] != '250':  # if the data is not received
      #print('250 reply not received from server.')



   # Send message data.
   subject = 'Subject: Testing SMTP Client \r\n'
   clientSocket.send(subject.encode())
   recv1 = clientSocket.recv(1024).decode()
   if recv1[:3] != '250':  # if the data is not received
      #print('250 reply not received from server.')


   # Message ends with a single period.
   clientSocket.send(('. \r\n').encode())
   recv1 = clientSocket.recv(1024).decode()
   if recv1[:3] != '250':  # if the data is not received
      #print('250 reply not received from server.')




   # Send QUIT command and get server response.
   quitcommand = ('QUIT \r\n')
   clientSocket.send(quitcommand.encode())
   recv1 = clientSocket.recv(1024).decode()



if __name__ == '__main__':
   smtp_client(1025, '127.0.0.1')

