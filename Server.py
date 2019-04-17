'''
Created on Sep 12, 2018

@author: Parth Mistry
'''

import socket
from _socket import AF_INET, SOCK_DGRAM

SERVERIP = "127.0.0.1"
SERVERPORT = 12000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((SERVERIP, SERVERPORT))

while (True):
    recvdMsg, clientAddr = s.recvfrom(2048)
    print ("Message is: " + recvdMsg.decode())
    s.sendto(recvdMsg.encode(), clientAddr)