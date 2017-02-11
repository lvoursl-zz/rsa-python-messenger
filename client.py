import socket
from Crypto.PublicKey import RSA
from config import HOST, PORT
 
def run_client():
    with open('server_public_key', 'r') as f:
        server_public_key = RSA.importKey(f.read())

    print(server_public_key)

    print('keys loaded \n')
     
    mySocket = socket.socket()
    mySocket.connect((HOST, PORT))
     
    message = str(input(" -> "))
     
    while message != 'q':
        print('message ' + message)
        
        message = server_public_key.encrypt(message.encode(errors='replace'), 32)[0]
        print('encrypted message' + str(message))
        mySocket.send(message)
        data = mySocket.recv(1024)
        
        print('data from server:' + str(data))
         
        message = input(" -> ")
             
    mySocket.close()
 
if __name__ == '__main__':
    run_client()