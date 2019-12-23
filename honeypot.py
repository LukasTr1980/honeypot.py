import socket
import atexit

# Local IP/Port for the honeypot to listen on (TCP)
LHOST = '0.0.0.0'
LPORT = 22

# Banner displayed when connecting to the honeypot
BANNER = b'SSH-2.0-OpenSSH_6.7p1\nLogin: '

# Socket timeout in seconds
TIMEOUT = 10

def main():
	print ('[*] Honeypot starting on ' + LHOST + ':' + str(LPORT))
	atexit.register(exit_handler)
	listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	listener.bind((LHOST, LPORT))
	listener.listen(5)
	while True:
		f = open('pot_log.txt', 'a')
		(insock, address) = listener.accept()
		insock.settimeout(TIMEOUT)
		print (f'[*] Honeypot connection from IP: {address[0]} on PORT: {address[1]}')
		f.write(f'[*] Honeypot connection from IP: {address[0]} on PORT: {address[1]}\n')
		try:
			insock.send(BANNER)
<<<<<<< HEAD
			data = insock.recv(8192)
			insock.send(b'User: ')
			data = insock.recv(8192)
			insock.send(b'Password: ')
			data = insock.recv(8192)
=======
			data = insock.recv(4096)
>>>>>>> 0b00a26ee6df041b4d307baa1011a0a0ee0f5743
		except socket.error as e:
			f.write(f'IP: {address[0]} with Error: {e}\n')
		else:
			f.write(f'IP: {address[0]}, with Data: {data}\n')
		finally:
			insock.close()
			f.close()

def exit_handler():
	print ('\n[*] Honeypot is shutting down!')
	listener.close()

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		pass
