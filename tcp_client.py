import socket

SERVER_IP = "127.0.0.1"
PORT = 8080

# Create TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect((SERVER_IP, PORT))

# Send data
client.send("HELLO SERVER".encode())

# Receive response
data = client.recv(1024)
print("server:", data.decode())

# Close connection
client.close()