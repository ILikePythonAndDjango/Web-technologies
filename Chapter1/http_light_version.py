# -*- coding: utf-8 -*-
import socket
import sys

tcp_port = 2020
server_ip_addr = "127.0.0.1"

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((server_ip_addr, tcp_port))
tcp.listen(20)

while True:
	connection, ip_addr = tcp.accept()
	print("Accept {}:{}".format(ip_addr, tcp_port))

	path = connection.recv(2048).decode("utf-8").rstrip()
	with open(str(path), 'r') as file:
		data = file.read().encode("utf-8")
	print("Body", path)
	print(data.decode("utf-8"))
	connection.sendall(data)
	connection.close()