# -*- coding: utf-8 -*-
import socket
import sys
from select import select

readsocks, writesocks = [], [] # sockets
while True:
		readables, writesocks, exceptions = \
			select(readsocks, writesocks, [])
		for sockobj in readables:
				data - sockobj.recv(1024)
				if not data:
					sockobj.close()
					readsocks.remove(sockobj)
				else:
					print('\tgot', data, 'on', id(sockobj))