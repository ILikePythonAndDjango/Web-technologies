import socket
import sys

tcp_port = 2020
client_ip_addr = "127.0.0.1"

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

for line in sys.stdin:
	line = line.rstrip()

	print("Please, input url: ", end="")

	# connection
	tcp.connect((client_ip_addr, tcp_port))
	tcp.send(line.encode("utf-8"))

	response = tcp.recv(1024*8)
	print("Body response:\n{}".format(response.decode("utf-8")))

	tcp.close()