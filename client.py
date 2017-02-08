import socket
from Crypto.PublicKey import RSA

 
def Main():
    # with open('server_private_key', 'r') as f:
    #     privkey = RSA.importKey(f.read())
    host = '127.0.0.1'
    port = 5000

    with open('server_public_key', 'r') as f:
        pubkey = RSA.importKey(f.read())

    print(pubkey)

    print('keys loaded \n')
     
    mySocket = socket.socket()
    mySocket.connect((host,port))
     
    message = str(input(" -> "))
     
    while message != 'q':
        print('message ' + message)
        
        message = pubkey.encrypt(message.encode(errors='replace'), 32)[0]
        mySocket.send(message)
        data = mySocket.recv(1024)
        
        print('data from server:' + str(data))
         
        message = input(" -> ")
             
    mySocket.close()
 
if __name__ == '__main__':
    Main()