import bluetooth
#import socket   

server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
port = 22
server_socket.bind(("",port))
server_socket.listen(1)

client_socket,address = server_socket.accept()
print ("Accepted connection from ",address)

while true:
    data = client_socket.recv(1024)   #앱에서 받은 데이터 프린트 (버튼 마다 a~h로 설정함..)
    print ("Received: %s" % data)

client_socket.close()
server_socket.close()
