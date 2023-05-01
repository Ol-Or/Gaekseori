import bluetooth

hostMACAddress = 'XX:XX:XX:XX:XX:XX' # 라즈베리파이 블루투스 MAC 주소
port = 1 # RFCOMM 포트 번호
backlog = 1
size = 1024

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind((hostMACAddress, port))
server_sock.listen(backlog)

client_sock, client_info = server_sock.accept()
print('Accepted connection from', client_info)

while True:
    data = client_sock.recv(size)
    if data.decode() == 'a':  #뚜껑 open
        print('Received: a')  
    if data.decode() == 'b':  #뚜껑 close
        print('Received: b')
    if data.decode() == 'c':  #차수판 up
        print('Received: c')
    if data.decode() == 'd':  #차수판 down
        print('Received: d')    
    if data.decode() == 'e':  #지붕 on
        print('Received: e')
    if data.decode() == 'f':  #지붕 off
        print('Received: f')
    if data.decode() == 'g':  #천장 on
        print('Received: g')
    if data.decode() == 'h':  #천장 off
        print('Received: h')
    elif not data:
        break

client_sock.close()
server_sock.close()
