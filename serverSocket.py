import socket
from concurrent import futures as cf


def run_server():

    def handle(sock: socket.socket, address: str):
        print(f'Connection established {address}')
        while True:
            received = sock.recv(1024)
            if not received:
                break
            message = received.decode()
            print(f'Data received: {message}')
            sock.send("OK".encode())
        print(f'Socket connection closed {address}')
        sock.close()

    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    port = 5050

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(2)

    with cf.ThreadPoolExecutor(2) as client_pool:

        try:
            while True:
                conn, address = server_socket.accept()
                client_pool.submit(handle, conn, address)
        except KeyboardInterrupt:
            print("Destroy server")
        finally:
            server_socket.close()


if __name__ == "__main__":
    run_server()
