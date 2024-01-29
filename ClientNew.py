import socket

def build_message(data_id, data):
    stx = b'\x4b\x32'  # STX (Start of Text) bytes
    etx = b'\x0d\x0a'  # ETX (End of Text) bytes

    # Length of ID + DATA in 3 bytes
    data_len = len(data_id.encode() + data.encode()).to_bytes(3, byteorder='big')  

    id_byte = data_id.encode()  # Convert ID to bytes

    # Calculate SUM 
    sum_byte = sum(data_id.encode() + data.encode()).to_bytes(2, byteorder='big')

    message = stx + data_len + id_byte + data.encode() + sum_byte + etx
    return message

def client_program():

    host = "***.***.**.**"  # IP
    port = 1404             # PORT

    client_socket = socket.socket()

    try:
        connect_option = input("Enter 1 to connect: ")

        if connect_option == '1':
            client_socket.connect((host, port))
            print("Connected to the Machine.")

        while True:
            data_id = input("Enter Data ID: ")
            data_body = input("Enter Data: ")

            if data_id.lower() == 'exit' or data_body.lower() == 'exit':
                break

            message = build_message(data_id, data_body)
            client_socket.send(message)

            response = client_socket.recv(1024).decode()
            print('Received from server:', response)

    except Exception as e:
        print(f"Connection failed: {e}")

    finally:
        client_socket.close()

if __name__ == '__main__':
    client_program()
