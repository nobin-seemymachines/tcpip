import socket
import threading

def handle_client(client_socket, client_address):
    print("Accepted connection from machine")
    try:
        data = client_socket.recv(1024)
        print("Received data from machine",data)
    except Exception as e:
        print(f"Error handling connection from machine")
    finally:
        client_socket.close()
        
def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(5)

    print(f"Server listening on port {port}")

    while True:
        client_socket, client_address = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == '__main__':
    start_server(1402)  
