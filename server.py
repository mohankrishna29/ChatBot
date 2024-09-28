import socket
import threading

clients = []
def broadcast(data, current_client):
    for i in clients:
        if i != current_client:
            i.send(data)

def start():
    server = socket.socket()
    server.bind(('0.0.0.0', 8080))
    print("Server Socket created")

    server.listen(2)
    print("Waiting for connections")

    while True:
        ip, addr = server.accept()
        clients.append(ip)
        print(f"Connected with {addr}")
        thread = threading.Thread(target = handle, args = (ip,))
        thread.start()


def handle(ip):
    while True:
        data = ip.recv(1024)
        if not data:
            continue
        broadcast(data, ip)
        # ip.send("Message received!".encode())
    ip.close()
    clients.remove(ip)




start()