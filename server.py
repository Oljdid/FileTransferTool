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




def receive_file_imcp():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 12345)) 

    f = open("recieved.txt", "wb")
    data = None
    while True:
        m = s.recv(1024)
        data = m
        if m:
            while m:
                m = s.recv(1024)
                data += m
            else:
                break
    f.write(data)
    f.close()
    print("Done receiving")

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
            receive_file_imcp()

        elif choice == "3":
            print("Exit")
            break
        else:
            print("Invalid choice")        

main()