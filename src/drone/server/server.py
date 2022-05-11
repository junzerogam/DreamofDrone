from socket import *
import time

port = 9000

serverSock = socket(AF_INET,SOCK_STREAM)
serverSock.bind(('',port))
serverSock.listen(1)
print('Waiting for connection %d port'%port)

connectionSock,addr = serverSock.accept()

print('Connected from ',str(addr))

while 1:
    distanceData = ""
    distanceData = connectionSock.recv(1024)
    print('distance = ',distanceData.decode('utf-8'))
    WeightData = ""
    WeightData = connectionSock.recv(1024)
    print('weight = ',WeightData.decode('utf-8'))