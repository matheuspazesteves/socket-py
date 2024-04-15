from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input('Input lowercase sentence:')
encoded_message = bytes(sentence, "utf-8")
clientSocket.send(encoded_message)
modifiedSentence = clientSocket.recv(1024)
print ('From Server: ', modifiedSentence)
clientSocket.close()
