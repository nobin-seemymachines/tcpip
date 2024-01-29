import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.0.102', 12345)
server_socket.bind(server_address)

server_socket.listen(1)

print('Server is listening on {}:{}'.format(*server_address))

while True:
    print('Waiting for a connection...')
    connection, client_address = server_socket.accept()
    
    try:
        print('Connection from', client_address)

        while True:
            data = connection.recv(1024)
            if not data:
                break
            print('Received data:', data.decode())
            connection.sendall(data)

    finally:
        connection.close()
