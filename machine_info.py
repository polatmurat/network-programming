import socket
import psutil

class MachineInfo:
    def __init__(self):
        self.hostname = socket.gethostname()
        self.ip_address = self.get_ip_address()
        self.network_interfaces = self.get_network_interfaces()

    def get_ip_address(self):
        for iface, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                if addr.family == socket.AF_INET:
                    return addr.address
        return None

    def get_network_interfaces(self):
        interfaces = psutil.net_if_addrs()
        return list(interfaces.keys())

    def display_info(self):
        print(f"Hostname: {self.hostname}")
        print(f"IP Address: {self.ip_address}")
        print(f"Network Interfaces: {', '.join(self.network_interfaces)}")
