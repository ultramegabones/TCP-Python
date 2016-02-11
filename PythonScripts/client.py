import socket
import sys  

try:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
  print 'Failed to create socket. Error code: ' + str(msg[0]) + ', Error message : ' + msg[1]
  sys.exit();

print 'Socket Created'

remote_ip = '192.168.1.10'
port = 8888

s.connect((remote_ip, port))

message = "MESSSAGEEEE\r\n\r\n"

try : 
  s.sendall(message)
except socket.error:
  print 'Send failed'
  sys.exit()

reply = s.recv(4096)

print reply

s.close()
print 'Connection Closed'
