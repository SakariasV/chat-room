import socket
import pickle


HEADER = 64
PORT = 50505
#IP = socket.gethostbyname(socket.gethostname())
IP = '192.168.1.180'

FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


def main():

    server_ip = socket.gethostname()

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP, PORT))
    text = 'PC here'
    send(client, text)



def send(client, msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_legth = str(msg_length).encode(FORMAT)
    send_legth += b' ' * (HEADER - len(send_legth))
    client.send(send_legth)
    client.send(message)

if __name__ == '__main__':
    main()
