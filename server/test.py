import socket
import threading


def send_mess():
    while True:
        mes = input()
        if mes == "exit":
            ya_sock.close()
            exit(0)
        ya_sock.send(mes.encode('ascii'))


def recieving():
    while True:
        data_chunk = ya_sock.recv(1024)
        data = data_chunk.decode()
        print(data)


ya_sock = socket.socket()
addr = ("127.0.0.1", 55555)
ya_sock.connect(addr)

name = input("Enter your name: ")
ya_sock.send(name.encode())


rec_thread = threading.Thread(target=recieving)
rec_thread.start()
send_thread = threading.Thread(target=send_mess)
send_thread.start()
