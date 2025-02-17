
import socket

target_host = "127.0.0.1"
port = 9998

#create a socket obj
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.connect((target_host, port))

#send some data
client.send(b"ABCD")	#"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#receive some data
response = client.recv(4096)

print(response.decode())
client.close
