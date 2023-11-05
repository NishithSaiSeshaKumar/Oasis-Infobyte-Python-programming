import socket
import threading

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('127.0.0.1', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(2)
print("Server is listening for incoming connections...")

# Create a list to store client connections and their names
clients = {}

def broadcast(message, sender_name):
    for client, name in clients.items():
        if name != sender_name:
            try:
                client.send((sender_name + ": " + message).encode())
            except:
                client.close()
                del clients[client]

def handle_client(client_socket, client_name):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(client_name + ": " + message)
            broadcast(message, client_name)
        except:
            break

    client_socket.close()
    del clients[client_socket]

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address[0]}:{client_address[1]}")

    # Receive the client's name
    client_name = client_socket.recv(1024).decode()
    print(f"{client_name} joined the chat")
    
    clients[client_socket] = client_name
    
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_name))
    client_thread.start()
