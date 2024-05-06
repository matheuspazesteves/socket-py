## Executar

- Primeiro verifique se o python3.9 está instalado:

```bash
python3 --version
```
- Caso não esteja instalado instalar v3.9 ou superior:
```bash
sudo apt-get update
sudo apt-get install git
sudo apt-get install python3-dotenv
```

- Segundo Clone o repositorio

```bash
sudo git clone https://github.com/matheuspazesteves/socket-py.git
```

- Abra a pasta:

- Executar o server (use python v3.9 ou superior:):

```bash
python3 TCPServer.py
```

- Executar o Client (use python v3.9 ou superior:):

```bash
python3 TCPClient.py
```


- ALTERAR A VARIAVEL DE AMBIENTE PARA CLIENTE CONECTAR A AWS:

```bash
SERVER_IP = 'IP DA MAQUINA DA AWS'
```


- MATHEUS PAZ ESTEVES E RODRIGO ALVES DA SILVA