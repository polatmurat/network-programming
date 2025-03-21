import socket
import struct
import time

class SNTPClient:
    def __init__(self, server='pool.ntp.org'):
        self.server = server
        self.time = None

    def get_time(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        address = (self.server, 123)
        message = b'\x1b' + 47 * b'\0'
        client.sendto(message, address)
        response, _ = client.recvfrom(1024)
        t = struct.unpack("!12I", response)
        timestamp = t[10] - 2208988800  # NTP time to Unix time
        self.time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(timestamp))
        print(f"Current time from NTP server {self.server}: {self.time}")
