import socket, threading
def handle_client(conn, addr): 
    print(f'[NEW] {addr} connected')
    while True:
        msg = conn.recv(1024)
        if not msg: 
            break
        cmd = msg.decode().strip()
        if cmd == 'ECHO': 
            conn.send(b'ECHO: message received')
        elif cmd == 'PING': 
            conn.send(b'PONG')
        else: 
            conn.send(b'MSG: ' + msg)
    conn.close()
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind(('0.0.0.0', 5555))
srv.listen()
while True:
    c, a = srv.accept()
    threading.Thread(target=handle_client, args=(c,a)).start()