# Computer Networks – Python Implementations

A collection of Python programs demonstrating core computer networking concepts, including error detection algorithms and socket-based communication.

## Contents

### Error Detection

| File | Description |
|------|-------------|
| `1dparity.py` | 1D even parity bit – adds a parity bit to a binary string and verifies it |
| `2dparity.py` | 2D parity check – computes row and column parity bits for a 2D bit matrix |
| `checksum.py` | 16-bit Internet checksum – sums binary data segments with carry-folding |
| `crc.py` | Cyclic Redundancy Check (CRC) – XOR-based polynomial division for error detection |

### TCP Socket Programs

| File | Description |
|------|-------------|
| `tcp_server.py` | Basic TCP server that accepts one connection, receives a message, and sends a reply (port 8080) |
| `tcp_client.py` | Basic TCP client that sends `"HELLO SERVER"` and prints the server's response |
| `tcpchat_server.py` | Multi-client TCP chat server that handles `ECHO` and `PING` commands via threads (port 5555) |
| `tcpchat_client.py` | Interactive TCP chat client – type commands and see the server's responses |

### UDP Socket Programs

| File | Description |
|------|-------------|
| `udp_server.py` | Basic UDP server that receives one datagram and sends a reply (port 8080) |
| `udp_client.py` | Basic UDP client that sends `"HELLO SERVER"` and prints the server's response |
| `udpecho_server.py` | UDP echo/chat server supporting `PING → PONG`, `ECHO`, and free-form messages (port 6060) |
| `udpchat_client.py` | Interactive UDP client for sending commands to the echo server |

### File Transfer

| File | Description |
|------|-------------|
| `filetransfer_server.py` | TCP server that reads a requested filename and streams the file contents (port 7070) |
| `filetransfer_client.py` | TCP client that requests `testfile.txt` and saves the received data as `received_file.txt` |

## Requirements

- Python 3.6 or higher (walrus operator `:=` used in file transfer scripts)
- No third-party packages – only the Python standard library

## Usage

### Error Detection

Run any of the error detection scripts directly:

```bash
python 1dparity.py
python 2dparity.py
python checksum.py
python crc.py
```

### TCP Client-Server

Start the server first, then run the client in a separate terminal:

```bash
# Terminal 1
python tcp_server.py

# Terminal 2
python tcp_client.py
```

### TCP Chat

```bash
# Terminal 1
python tcpchat_server.py

# Terminal 2
python tcpchat_client.py
# Type commands like: ECHO, PING, or any message
```

### UDP Client-Server

```bash
# Terminal 1
python udp_server.py

# Terminal 2
python udp_client.py
```

### UDP Echo / Chat

```bash
# Terminal 1
python udpecho_server.py

# Terminal 2
python udpchat_client.py
# Type commands like: PING, ECHO <message>, or any text
```

### File Transfer

Create a `testfile.txt` in the server's working directory, then:

```bash
# Terminal 1
python filetransfer_server.py

# Terminal 2
python filetransfer_client.py
# Output saved as received_file.txt
```

## Port Reference

| Program | Protocol | Port |
|---------|----------|------|
| Basic TCP | TCP | 8080 |
| Basic UDP | UDP | 8080 |
| TCP Chat | TCP | 5555 |
| UDP Echo/Chat | UDP | 6060 |
| File Transfer | TCP | 7070 |
