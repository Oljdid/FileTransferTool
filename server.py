import socket
from scapy.all import DNSQR, sniff
import binascii

def receive_file_dns(packet):
    # Check if the packet has a DNS query
    if packet.haslayer(DNSQR):
        # Get the domain name from the query
        domain = packet[DNSQR].qname.decode()

        # Remove the '.example.com' suffix
        hex_data = domain.replace('.example.com', '')

        try:
            # Decode the file data
            file_data = binascii.unhexlify(hex_data)

            # Write the file data to a file
            with open('received_file.txt', 'ab') as file:
                file.write(file_data)
        except binascii.Error:
            print(f"Non-hexadecimal data found: {hex_data}")




def receive_file_imcp(server_ip, server_port, file_path):
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address
    server_socket.bind((server_ip, server_port))

    # Listen for incoming connections
    server_socket.listen(1)

    while True:
        # Wait for a connection
        print('waiting for a connection')
        client_socket, client_address = server_socket.accept()

        # Receive the file and write it to disk
        with open(file_path, 'wb') as file:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                file.write(data)

        # Clean up the connection
        client_socket.close()
def display_menu():
    print("1. Receive a file by DNS ")
    print("2. Receive a file by IMCP ")
    print("3. Exit ")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            sniff(filter='udp port 53', prn=receive_file_dns)
        elif choice == "2":
            receive_file_imcp('localhost', 12345, 'received_file.txt')

        elif choice == "3":
            print("Exit")
            break
        else:
            print("Invalid choice")        

main()