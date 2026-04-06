import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 6060))
while True:
    data, addr = s.recvfrom(1024)
    msg = data.decode().strip()
    if msg == 'PING': 
        s.sendto(b'PONG', addr)
    elif msg.startswith('ECHO'): 
        s.sendto(data, addr)
    else: 
        s.sendto(b'TALk:' + data, addr)