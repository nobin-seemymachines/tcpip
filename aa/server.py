import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('0.0.0.0', 12345)
server_socket.bind(server_address)

server_socket.listen(1)

print('Server is listening on {}:{}'.format(*server_address))

while True:
    print('Waiting for a connection...')
    connection, client_address = server_socket.accept()
    
    try:
        print('Connection from', client_address)

        data = connection.recv(1024).decode()
        
        print('Received data:', data)
        connection.send(data.encode())

    finally:
        connection.close()
