import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    msg = input('CMD: ')
    s.sendto(msg.encode(), ('127.0.0.1', 6060))
    print(s.recvfrom(1024))