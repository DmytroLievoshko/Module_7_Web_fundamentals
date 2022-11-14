import socket


def run_client():

    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    port = 5050

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((ip, port))

    try:
        message = input("input message >> ")

        client_socket.send(message.encode())

        response = client_socket.recv(1024)
        print(f'Response data: {response.decode()}')

    except KeyboardInterrupt:
        print("Destroy server")
    finally:
        print(f'Data transfer completed')
        client_socket.close()


if __name__ == "__main__":
    run_client()
