import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.29.21', 12345)

try:
    client_socket.connect(server_address)
    message = 'Hello, server!'
    msg ="close"
    client_socket.sendall(message.encode())
    print('connected ')

    data = client_socket.recv(1024)
    print('Received data:', data.decode())

finally:
    # Clean up the connection
    client_socket.close()
