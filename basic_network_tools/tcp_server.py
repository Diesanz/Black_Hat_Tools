import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def main():
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind((IP, PORT)) #pass ip and port we wanted to listening
	server.listen(5) #start listener

	print(f'[*] Listening on {IP}: {PORT}')

	while True: #waits incoming connections
		client, address = server.accept() #received client socket and remote connection details
		print(f'[*] Accepted connection form {address[0]}: {address[1]}')

		client_handler = threading.Thread(target=handle_client, args=(client,)) #create a thread obj that points to the client, asing the function to the thread
		client_handler.start() #handle client connection

def handle_client(client_socket): #performs the recv() and send a msg
	with client_socket as sock: #use of with close automatiaclly the socket
		request = sock.recv(1024)
		print(f'[*] Received: {request.decode("utf-8")}')
		sock.send(b'ACK')

if __name__ == '__main__' :
	main()
