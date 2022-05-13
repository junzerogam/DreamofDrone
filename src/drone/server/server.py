from socket import *

port = 9000

# tcp
serverSock = socket(AF_INET, SOCK_STREAM)

# bind
serverSock.bind(('', port))

# listen
serverSock.listen(5)
print('Waiting for connection %d port' % port)

# accept
connectionSock, addr = serverSock.accept()
print('Connected from ',str(addr))

# recv and print
while 1:
    nothing = "Null"

    weightData = ""
    weightData = connectionSock.recv(1024)
    print("weight = %s g" %(weightData.decode('utf-8')))
    connectionSock.send(nothing.encode('utf-8'))

    distanceData = ""
    distanceData = connectionSock.recv(1024)
    print("distance = %s cm" %(distanceData.decode('utf-8')))
    connectionSock.send(nothing.encode('utf-8'))

    volumePercentage = ""
    volumePercentage = connectionSock.recv(1024)
    print("percentage = %s %%\n" %(volumePercentage.decode('utf-8')))
    connectionSock.send(nothing.encode('utf-8'))
