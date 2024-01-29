import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Print client's IP address before connecting
client_ip = socket.gethostbyname(socket.gethostname())
print('Client IP:', client_ip)

server_address = ('192.168.29.21', 12345)

try:
    client_socket.connect(server_address)
    message = 'Hello, server!'
    msg = "close"
    client_socket.sendall(message.encode())
    print('Connected to server at', server_address)

    # Print server's IP address after connecting
    server_ip = socket.gethostbyaddr(server_address[0])[0]
    print('Server IP:', server_ip)

    # Receive the response from the server
    data = client_socket.recv(1024)
    print('Received data:', data.decode())

finally:
    # Clean up the connection
    client_socket.close()
