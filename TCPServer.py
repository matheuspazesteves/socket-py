import os
import socket
import pickle
from functools import reduce
from dotenv import load_dotenv
load_dotenv();

def handle_client(client_socket):
    request = client_socket.recv(1024)
    data = pickle.loads(request)
    numbers = list(map(float, data['numeros'].split()))
    operation = data['operacao']

    if operation == '+':
        result = sum(numbers)
    elif operation == '-':
        result = reduce(lambda x, y: x - y, numbers)
    elif operation == '*':
        result = 1
        for num in numbers:
            result *= num
    elif operation == '/':
        if numbers[1] == 0:
            result = "Impossivel dividir por 0"
        else:
            result = numbers[0] / numbers[1]
    else:
        result = "Operação inválida"

    client_socket.send(str(result).encode())
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((os.getenv("SERVER_LOCAL"), int(os.getenv("SERVER_PORT"))))
    server.listen(5)
    print("Servidor da Calculadora iniciado. Aguardando conexões...")

    while True:
        client_socket, addr = server.accept()
        print(f"Conexão recebida de {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    main()
