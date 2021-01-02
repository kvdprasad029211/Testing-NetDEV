import socket

HOST = '127.0.0.1'
PORT = 12345

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as dd:

	dd.connect((HOST,PORT))
	dd.sendall(b'Hello, world')
	data = dd.recv(1024)
	
	print ('recvd', repr(data))
					