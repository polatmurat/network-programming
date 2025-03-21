from machine_info import MachineInfo
from echo_test import EchoTest
from sntp_client import SNTPClient
from simple_chat import SimpleChat
from socket_settings import SocketSettings

def main():
    while True:
        print("\nMain Menu:")
        print("1. Machine Information")
        print("2. Echo Test")
        print("3. SNTP Time Check")
        print("4. Chat")
        print("5. Error Management")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            machine_info = MachineInfo()
            machine_info.display_info()
        elif choice == '2':
            host = input("Enter server IP: ")
            port = int(input("Enter port: "))
            echo_test = EchoTest(host, port)
            mode = input("Enter mode (client/server): ")
            if mode == 'server':
                echo_test.server()
            elif mode == 'client':
                echo_test.client()
        elif choice == '3':
            sntp = SNTPClient()
            sntp.get_time()
        elif choice == '4':
            host = input("Enter server IP: ")
            port = int(input("Enter port: "))
            chat = SimpleChat(host, port)
            mode = input("Enter mode (client/server): ")
            if mode == 'server':
                chat.server()
            elif mode == 'client':
                chat.client()
        elif choice == '5':
            host = input("Enter server IP: ")
            port = int(input("Enter port: "))
            socket_settings = SocketSettings(host, port)
            action = input("Enter action (timeout/non-blocking): ")
            if action == 'timeout':
                timeout = int(input("Enter timeout value in seconds: "))
                socket_settings.set_socket_timeout(timeout)
            elif action == 'non-blocking':
                socket_settings.set_non_blocking()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
