import socket

class EchoTest:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen(1)
            print("Server is listening...")
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024)
                if data:
                    conn.sendall(data)
                    print("Data sent back to client.")

    def client(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.host, self.port))
            message = "Hello, Server"
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print(f"Received from server: {data.decode()}")
            if message == data.decode():
                print("Connection successful, data matches.")
            else:
                print("Data mismatch.")
