import os
import socket
import pickle
from dotenv import load_dotenv

load_dotenv();


def main():
    server_ip = os.getenv("SERVER_IP")
    server_port = int(os.getenv("SERVER_PORT"))

    while True:
        operation = input("Escolha a operação (+, -, *, /) ou 'sair' para encerrar: ")
        if operation.lower() == 'sair':
            break

        numbers = input("Digite os números separados por espaço: ")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        message = {
            'operacao': operation,
            'numeros': numbers
        }
        data=pickle.dumps(message)
        client_socket.connect((server_ip, server_port))
        client_socket.send(data)

        result = client_socket.recv(1024).decode()
        print(f"Resultado: {result}")

        client_socket.close()

if __name__ == "__main__":
    main()
