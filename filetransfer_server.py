import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 7070))
s.listen(1)
conn, _ = s.accept()
filename = conn.recv(1024).decode()
with open(filename, 'rb') as f:
    while chunk := f.read(4096):
        conn.send(chunk)
conn.close()