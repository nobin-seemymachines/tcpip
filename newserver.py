import socket
import time
import json

# Read data from the JSON file
with open("data.json", "r") as json_file:
    data_dict = json.load(json_file)

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
host = socket.gethostname()
port = 1401
print(socket.gethostbyname(host))
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)

print(f"Server listening on {host}:{port}")

while True:
    # Wait for a connection from the client
    print("Waiting for a connection...")
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Receive data from the client
    data_request = client_socket.recv(1024).decode('utf-8')
    print(f"Received data request: {data_request}")

    # Check if the received data is a request for all values
    if data_request.lower() == "all":
        # Send all values to the client
        for key, value in data_dict.items():
            client_socket.send(f"{key}: {value}".encode('utf-8'))
            time.sleep(1)  # Add a small delay between sending each value

        # Signal the end of data
        client_socket.send("end_of_data".encode('utf-8'))

    else:
        # Check if the received data is in the data dictionary
        if data_request in data_dict:
            # Fetch corresponding data based on the client's request
            response = data_dict[data_request]
            # Send the response back to the client
            client_socket.send(response.encode('utf-8'))
        else:
            response = "Error: Invalid input."
            # Send the response back to the client
            client_socket.send(response.encode('utf-8'))

    # Close the connection with the client
    client_socket.close()

    # Wait for 30 seconds for the next connection
    time.sleep(30)
    print("Server disconnected due to inactivity.")