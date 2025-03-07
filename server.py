import socket
from threading import Thread

IP_ADDRESS ='127.0.0.1'
PORT = 8050
SERVER - None
BUFFER_SIZE = 4096
clients = {}

def setup():
    print("\n\t\t\t\t\t\tIP MESSENGER\n")
    global values
    global PORT
    global IP_ADDRESS
    global SERVER
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    print("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...") 
    print("\n")

def acceptConnections():
    global SERVER
    global clients
    while True:
        client, addr = SERVER.accept()
        print(client.addr)

def setup():
    print("\n\t\t\t\t\t\tIP MESSENGER\n")
    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    SERVER.bind((IP_ADDRESS, PORT))
    SERVER.listen(100)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...")
    print("\n")

    acceptConnections()

    setup_thread  = Thread(target = setup)
    setup_thread.start()

def acceptConnections():
    global SERVER
    global clients
    while True:
        client, addr = SERVER.accept()
        client_name = client.recv(4096).decode().lower()
        clients[client_name] = {
            "client": client,
            "address": addr,
            "connected_with" : "",
            "file name" : "",
            "file size": 4096
        }
        print(f"Connection established with (client_name): (addr)")
        thread = Thread(target = handleClient, args = (client,client_name,))
        thread.start()