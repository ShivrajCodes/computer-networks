import socket
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(('127.0.0.1', 7070))
c.send(b'testfile.txt')
with open('received_file.txt', 'wb') as f:
    while data := c.recv(4096):
        f.write(data)
c.close()
print('File transfer complete.')