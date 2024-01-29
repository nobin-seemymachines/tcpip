import socket

def send_request():
    host = "192.168.0.101"  # Replace with the actual IP address of EXA_ES
    port = 1401  # Replace with the actual port number

    stx = b'\x4b'  
    etx = b'\x0d\x0a'  # ETX (End of Text) bytes
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        print("Connected to EXA_ES.")

        request = stx + etx  # Encode the data
        client_socket.send(request)

        response = client_socket.recv(1024)
        print('Received from ', response.decode())

    except Exception as e:
        print(f"Connection failed: {e}")

    finally:
        client_socket.close()

if __name__ == '__main__':
    send_request()
