import socket
import threading

HOST = "127.0.0.1"
PORT = 55555


def server_conn(sock, addr):
    with sock:
        client = (conn.recv(1024)).decode()
        print(f"Connected by {client}")
        send_message(client.encode() + " joined".encode())
        while True:
            try:
                data = sock.recv(1024)
                if not data:
                    break
                if data == b"exit":
                    break
                print(client + ": " + data.decode())
                data = client.encode() + ": ".encode() + data
                data = data.upper()
                send_message(data)
            except socket.error:
                print(f"{addr} disconnected")
                my_users.pop(addr)
                send_message(f"{client} has left.")
                return


def send_message(message):
    for sock in my_users.values():
        sock.send(message)


if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serv_sock:
        serv_sock.bind((HOST, PORT))
        serv_sock.listen()
        print("Server started")
        my_users = {}
        while True:
            conn, addr = serv_sock.accept()
            if not my_users.get(addr):
                my_users[addr] = conn
            t = threading.Thread(target=server_conn, args=(conn, addr))
            t.start()
