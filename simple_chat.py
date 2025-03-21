import socket
import json

class SimpleChat:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.messages = []

    def save_message(self, message):
        self.messages.append(message)
        with open('chat_history.json', 'w') as file:
            json.dump(self.messages, file)

    def server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen(1)
            print("Chat server is listening...")
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    message = data.decode()
                    print(f"Received: {message}")
                    self.save_message(message)
                    conn.sendall(data)

    def client(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))
            while True:
                message = input("Enter message: ")
                client_socket.sendall(message.encode())
                data = client_socket.recv(1024)
                print(f"Server says: {data.decode()}")
                self.save_message(message)
