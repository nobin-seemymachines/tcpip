import socket

def client_program():
    
    host = "192.168.29.230"  #IP address
    port = 1401             #Port number

    client_socket = socket.socket()
    try:
        connect_option = input("Enter 1 to connect: ")

        if connect_option == '1':
            client_socket.connect((host, port))
            print("Connected to the Machine.")
            while True:
                message = input("Enter a Request to send to the Machine (type 'exit' to close): ")
                if message.lower() == 'exit':
                    break
                hex_message = message.encode().hex()

                client_socket.send(bytes.fromhex(hex_message))
                data = client_socket.recv(1024).decode()
                print('Received from Machine:', data)

        else:
            print("Not Connected")

    except Exception as e:
        print(f"Connection failed: {e}")

    finally:
        client_socket.close()

if __name__ == '__main__':
    client_program()
