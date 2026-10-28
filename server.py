import socket
import threading
import time


HEADER = 64
PORT = 50505
#IP = socket.gethostbyname(socket.gethostname())
IP = '192.168.1.180'
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


def main():
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))

    server.listen(5)


    while True:
        listen(server)

def listen(server):
    print(f"[server listening on {IP}]")
    while True:
        client, addr = server.accept()
        thread = threading.Thread(target=handle_client, args= (client, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


def handle_client(client, addr):

    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        msg_length = client.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = client.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                msg = "[User left]"
                connected = False
        
        print(f"[{client}] {msg}")
        time.sleep(2)

    client.close()











if __name__ == '__main__':
    main()