import socket
import json

def read_input(file_path):
    with open(file_path, 'r') as json_file:
        messages = json.load(json_file)
    return list(messages.keys())

def get_machine_details(port,host):
    # machine_ip = socket.gethostbyname(socket.gethostname())
    machine_ip = host
    machine_port = port 
    return {'machine_ip': machine_ip, 'machine_port': machine_port}

def client_program():
    host = socket.gethostname()  
    # host = "192.168.29.17"
    #   #host address of server
    port = 1401
    client_socket = socket.socket()
    client_socket.connect((host, port))

    input_file_path = 'inputs.json'  
    output_file_path = 'responses.json'  

    messages = read_input(input_file_path)
    responses = {}
    responses.update(get_machine_details(port,host))

    if messages is not None:
        for message in messages:
            client_socket.send(message.encode())
            data = client_socket.recv(1024).decode()
            print('Received from server for {}: {}'.format(message, data))
            responses[message] = data

        # Save responses to a JSON file
        with open(output_file_path, 'w') as json_file:
            json.dump(responses, json_file, indent=2)

    client_socket.close()

if __name__ == '__main__':
    client_program()
