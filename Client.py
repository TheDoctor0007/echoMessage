'''
Created on Sep 12, 2018

@author: Parth Mistry
'''

import socket
from _socket import AF_INET, SOCK_DGRAM

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

SERVERIP = "127.0.0.1"
SERVERPORT = 12000
msgLen = 10


msg = "1234567890"
n = 0
recvdMsg = None;
s.sendto(msg.encode(), (SERVERIP, SERVERPORT))
while (n < 3 and recvdMsg is None):
    recvdMsg, serverAddr = s.recvfrom(2048)
    n+=1
    s.sendto(msg.encode(), (SERVERIP, SERVERPORT))
print ("Message is: " + recvdMsg.decode())
s.close()