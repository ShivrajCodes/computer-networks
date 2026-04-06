import socket
SERVER_IP="127.0.0.1"
PORT=8080
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto("HELLO SERVER".encode(), (SERVER_IP, PORT))
data, _ = client.recvfrom(1024)
print("server:",data.decode())