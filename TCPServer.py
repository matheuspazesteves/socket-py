import os
import socket
import pickle
from functools import reduce
from dotenv import load_dotenv
load_dotenv();

def handle_client(client_socket, addr):
    request = client_socket.recv(1024)
    data = pickle.loads(request)
    if(len(data['numeros']) == 0):
        client_socket.send('Sem números'.encode())
        print(f"Conexão encerrada de {addr}")
        client_socket.close()
        return
    if(len(data['numeros']) == 1):
        client_socket.send('Somente um número'.encode())
        print(f"Conexão encerrada de {addr}")
        client_socket.close()
        return
    numbers = list(map(float, data['numeros'].split()))
    if len(numbers) > 20:
        client_socket.send('Quantidade de números não pode ser maior que 20'.encode())
        print(f"Conexão encerrada de {addr}")
        client_socket.close()
        return
    operation = data['operacao']

    if operation == '+':
        result = reduce(lambda x, y: x + y, numbers)
    elif operation == '-':
        result = reduce(lambda x, y: x - y, numbers)
    elif operation == '*':
        result = reduce(lambda x, y: x * y, numbers)
    elif operation == '/':
        if numbers[1] == 0:
            result = "Impossivel dividir por 0"
        else:
            result = numbers[0] / numbers[1]
    else:
        result = "Operação inválida"

    client_socket.send(str(result).encode())
    print(f"Conexão encerrada de {addr}")
    client_socket.close()
    return

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((os.getenv("SERVER_LOCAL"), int(os.getenv("SERVER_PORT"))))
    server.listen(1)
    print("Servidor iniciado. Aguardando conexões...")

    while True:
        client_socket, addr = server.accept()
        print(f"Conexão recebida de {addr}")
        handle_client(client_socket, addr)

if __name__ == "__main__":
    main()
