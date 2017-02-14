import socket
from Crypto.PublicKey import RSA
from config import HOST, PORT
 
def run_client():
    # загружаем публичный ключ сервера
    with open('server_public_key', 'r') as f:
        server_public_key = RSA.importKey(f.read())
    # загружаем приватный ключ клиента
    with open('client_private_key', 'r') as f:
        client_private_key = RSA.importKey(f.read())

    print('keys loaded \n')
     
    # создаем соединение и подключаемся к серверу
    mySocket = socket.socket()
    mySocket.connect((HOST, PORT))
    
    message = input(" -> ")
     
    while message != 'q':
        print('message ' + message)
        
        # шифруем сообщение публичным ключом сервера
        message = server_public_key.encrypt(message.encode(errors='replace'), 32)[0]
        print('encrypted message' + str(message))
        mySocket.send(message)
        
        # получаем данные от сервера и декодируем их своим приватным ключом
        data = mySocket.recv(1024)
        data = client_private_key.decrypt(data)

        print('data from server:' + str(data))
         
        message = input(" -> ")
             
    mySocket.close()
 
if __name__ == '__main__':
    run_client()
