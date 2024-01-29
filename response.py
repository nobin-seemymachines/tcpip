import socket


def receive_and_extract(socket):
    try:
        while True:
            message= input("Enter data : ");
            data = socket.recv(1024).encode()
            if not data:
                break

            
            print("Received and Extracted Data:")
            print(data)

    except Exception as e:
        print(f"Error receiving data: {e}")

def client_program():
    host = "192.168"  # Replace with the actual IP address of your server
    port = 1401  # Replace with the actual port number

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        print("Connected to the server.")

        # Start a thread or a separate process for receiving and processing data
        receive_and_extract(client_socket)

    except Exception as e:
        print(f"Connection failed: {e}")

    finally:
        client_socket.close()

if __name__ == '__main__':
    client_program()
