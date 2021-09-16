#! /usr/bin/env python3
import socket
from multiprocessing import Pool

# define address, buffer size
HOST = "localhost"
PORT = 8001
BUFFER_SIZE = 1024

payload = "GET / HTTP/1.0\r\nHosr: www.google.com\r\n\r\n"


def connect(addr):
	# create socket, connect, and receive data
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(addr)
		s.sendall(payload.encode())
		s.shutdown(socket.SHUT_WR) #shutdown() is different from close()

		full_data = s.recv(BUFFER_SIZE)
		print(full_data)

	except Exception as e:
		print(e)

	finally:
		# remember to close
		s.close()


def main():
	address = [(HOST, PORT)]
	with Pool() as p:
		p.map(connect, address * 3)


if __name__ == "__main__":
	main()