import socket

SERVER_IP = "0.0.0.0"
PORT = 8080

# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind and listen
server.bind((SERVER_IP, PORT))
server.listen(1)

print("TCP server listening...")

# Accept connection
conn, addr = server.accept()
print("Connected by:", addr)

# Receive data
data = conn.recv(1024)
print("client:", data.decode())

# Send response
conn.send("Message received".encode())

# Close connection
conn.close()