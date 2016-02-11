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

f = open('/home/udooer/test.txt','rb')
print 'Sending...'
l = f.read(1024)
while (l):
    print 'Sending...'
    s.send(l)
    l = f.read(1024)
f.close()
print "Done Sending"
print s.recv(1024)  

s.close()
print 'Connection Closed'
