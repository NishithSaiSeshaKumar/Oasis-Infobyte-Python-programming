import socket
import threading

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('127.0.0.1', 12345)
client_socket.connect(server_address)

# Enter your name
client_name = input("Enter your name: ")
client_socket.send(client_name.encode())

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            print("Connection lost.")
            client_socket.close()
            break

def send_messages():
    while True:
        message = input()
        client_socket.send(message.encode())

receive_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)

receive_thread.start()
send_thread.start()
