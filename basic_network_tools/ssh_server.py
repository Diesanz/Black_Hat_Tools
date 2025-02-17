import os
import paramiko
import socket
import sys
import threading

CWD = os.path.dirname(os.path.realpath(__file__)) #ruta al directorio donde esta el script
HOSTKEY = paramiko.RSAKey.from_private_key_file(os.path.join(CWD, 'test_rsa.key')) #carga la clave privada

class Server(paramiko.ServerInterface):
    def __init__(self): 
        self.event = threading.Event() #manejar eventos de sincronizacion de hilo

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, passwd):
        if username == 'diego' and passwd == 'seckret':
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

if __name__ == '__main__':
    server = '192.168.1.100'
    ssh_port = 2222
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((server, ssh_port))
        sock.listen(100)
        print('[+] Listening for connection...')
        
        client, addr = sock.accept()
        print('[+] Got a connection!', client, addr)

        bhSession = paramiko.Transport(client) #crea un sesion ssh sobre la conexion establecida
        bhSession.add_server_key(HOSTKEY) #us clave priv para autentificar
        server = Server()
        bhSession.start_server(server=server) #inicia servidor con configuracion de la clase Servidor

        chan = bhSession.accept(20)
        if chan is None:
            print('*** No Channel')
            sys.exit(1)

        print('[+] Authenticated!')
        print(chan.recv(1024).decode())
        chan.send('Welcome to bh_ssh'.encode())

        try:
            while True:
                command = input("Enter a command: ")
                if command != 'exit':
                    chan.send(command.encode())
                    r = chan.recv(8192)
                    print(r.decode())
                else:
                    chan.send('exit'.encode())
                    print('Exiting...')
                    bhSession.close()
                    break
        except KeyboardInterrupt:
            bhSession.close()
    except Exception as e:
        print('[-] Listen failed:', str(e))
        sys.exit(1)
