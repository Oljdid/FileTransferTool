import socket
from scapy.all import DNSQR, sniff, ICMP
import binascii


def receive_file_dns():
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect(("AdresseIpEnvoyeur", 12345))
   data = s.recv(1024)
   print(f"Received from server: {data.decode()}")
   s.close()


def receive_file_icmp():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect(("AdresseIpEnvoyeur", 12343))  # Connect to the server
  with open("received_file.txt", "wb") as f:
      while True:
          data = s.recv(1024)
          if not data:
              break  # The file has been completely received
          print(data)
          f.write(data)




  print("Done receiving...")
  s.close()








def display_menu():
   print("1. Receive a file by DNS ")
   print("2. Receive a file by ICMP ")
   print("3. Exit ")


def main():
   while True:
       display_menu()
       choice = input("Enter your choice: ")
       if choice == "1":
           receive_file_dns()
       elif choice == "2":
           receive_file_icmp()
       elif choice == "3":
           print("Exit")
           break
       else:
           print("Invalid choice")       


main()






