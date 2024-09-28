# Client side functioning
# Type exit to end the chat

import socket

def start_client():
    client = socket.socket()
    client.connect(("localhost", 8080))

    while True:
        message = input("You : ")
        if message == "exit":
            break
        client.sendall(message.encode())
        response = client.recv(1024).decode()
        print(f"AI : {response}")
    client.close()

start_client()