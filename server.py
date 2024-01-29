import socket
import json

def load_data(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def server_program():
    host = socket.gethostname()
    port = 1401
    print(socket.gethostbyname(host))

    server_socket = socket.socket()  
    server_socket.bind((host, port)) 
    server_socket.listen(1)
    conn, address = server_socket.accept() 
    print("Connection from: " + str(address))

    datas = load_data('data.json')

    while True:
        try:
            request = conn.recv(1024).decode()
            if not request:
                break
            print("Request: " + str(request))
            if request in datas:
                conn.send(datas[request].encode())
            else:
                conn.send("Error: Request not found in data".encode())
        except socket.error as e:
            print(f"Socket error: {e}")
            break

    conn.close()

if __name__ == '__main__':
    server_program()
