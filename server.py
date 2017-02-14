# импортируем библиотеки для сетевого взаимодействия и шифрования
import socket
from Crypto.PublicKey import RSA
from config import HOST, PORT
 
def run_server():
    # загружаем приватный ключ сервера
    with open('server_private_key', 'r') as f:
        server_private_key = RSA.importKey(f.read())

    # загружаем публичный ключ клиента
    with open('client_public_key', 'r') as f:
        client_public_key = RSA.importKey(f.read())
            
    print('key loaded \n')

    # сокет и привязываем его к определенному адресу
    mySocket = socket.socket()
    mySocket.bind((HOST, PORT))
     
    # ждем подключения 
    mySocket.listen(5)
    
    # подключение состоялось
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
        # получаем данные от клиента
        data = conn.recv(1024)
        if not data:
            break

        # дешифруем данные своим приватным ключом
        data = server_private_key.decrypt(data)
        print ("i get it from client after encryption: " + str(data))

        # вводим сообщение с клавиатуры, и шифруем его публичным ключом клиента
        message = input(" -> ")
        message = client_public_key.encrypt(message.encode(errors = 'replace'), 32)[0]
        
        # отправляем данные клиенту
        conn.send(message)
    # закрываем соединение     
    conn.close()
     
if __name__ == '__main__':
    # запускаем главную функцию
    run_server()
