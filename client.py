import socket

def main():

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 9999))
        client.send('client connected'.encode())
        print(client.recv(1024).decode())
    except:
        print("Failed connecting to the server")

    while True:
        pass


if __name__ == '__main__':
    main()
