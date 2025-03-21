import socket

class SocketSettings:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def set_socket_timeout(self, timeout):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            try:
                s.connect((self.host, self.port))
                print("Connection successful.")
            except socket.timeout:
                print(f"Connection timed out after {timeout} seconds.")
            except socket.error as e:
                print(f"Socket error: {e}")

    def set_non_blocking(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setblocking(False)
            try:
                s.connect((self.host, self.port))
                print("Connection successful.")
            except socket.error:
                print("Non-blocking connection error.")
