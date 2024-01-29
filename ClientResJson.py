import socket
import time
import json

def send_request():
    host = "192.168.0.101"  # Replace with the actual IP address 
    port = 1401  # Replace with the actual port number

    stx = b'\x4b'  # STX (Start of Text) byte
    etx = b'\x0d\x0a'  # ETX (End of Text) bytes        
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    responses = {}

    try:
        client_socket.connect((host, port))
        print("Connected to EXA_ES.")

        for i in range(1, 10):  
            
            request = stx + etx
            client_socket.send(request)

            response = client_socket.recv(2056)
            hex_response = response.hex()
            print(f"Response {i} from machine:", hex_response)

            # Add response to the dictionary with key 1 to 20
            responses[i] = {"hex_response": hex_response}

            # Wait for 10 seconds before sending the next request
            time.sleep(2)

        # Save all responses to JSON file
        with open("responses.json", "w") as json_file:
            json.dump(responses, json_file)

        print("All responses saved to responses.json")

    except Exception as e:
        print(f"Connection failed: {e}")

    finally:
        client_socket.close()

if __name__ == '__main__':
    send_request()
