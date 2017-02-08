import socket
from Crypto.PublicKey import RSA
 
def Main():
    host = "127.0.0.1"
    port = 5000

    with open('server_private_key', 'r') as f:
        privkey = RSA.importKey(f.read())

    print('key loaded \n')

    mySocket = socket.socket()
    mySocket.bind((host,port))
     
    mySocket.listen(5)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
        data = conn.recv(1024)
        if not data:
                break

        d = privkey.decrypt(data)

        print ("i get it from client after encryption: " + str(d))
        conn.send(d)
             
    conn.close()
     
if __name__ == '__main__':
    Main()