import socket
SERVER_IP="0.0.0.0"
PORT=8080
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((SERVER_IP, PORT))
print('UDP server listening...')
data, addr=server.recvfrom(1024)
print("client:",data.decode())
server.sendto("Message recieved".encode(), addr)