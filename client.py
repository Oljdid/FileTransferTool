import socket
import os
from scapy.all import DNS, DNSQR, IP, send, UDP, ICMP
import binascii

def display_menu():
    print("1. Send a file by DNS ")
    print("2. Send a file by ICMP ")
    print("3. Exit ")

def send_file_dns():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("adresseIpReceveur", 12345))
    server_socket.listen(1)
    print("Server listening on port 12345...")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode()
        print(f"Received from client: {message}")
 
        client_socket.sendall(data)
        client_socket.close()
    server_socket.close()


def send_file_icmp():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("adresseIpReceveur", 12343))
    s.listen(1)
    c, addr = s.accept()
    print('{} connected.'.format(addr))

    with open("file.txt", "rb") as f:
        m = f.read()
        print(m)
        c.sendall(m)
    print("Done sending...")
    c.close()  
    s.close()  

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            send_file_dns()
            break
        elif choice == "2":
            send_file_icmp()
            break
        elif choice == "3":
            print("Exit")
            break
        else:
            print("Invalid choice")

main()
