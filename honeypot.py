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
        (insock, address) = listener.accept()
        insock.settimeout(TIMEOUT)
        print ('[*] Honeypot connection from ' + address[0] + ':' + str(address[1]) + ' on port ' + str(LPORT))
        try:
            insock.send(BANNER)
            data = insock.recv(1024)
        except socket.error as e:
            writeLog(address[0],'Error: ' + str(e))
        else:
            writeLog(address[0],data)
        finally:
            insock.close()

def writeLog(fromip, message):
    f = open('pot_log.txt', 'a')
    f.write('IP:' + fromip + ' Port:' + str(LPORT) + ' | ' + message.replace('\r\n', ' ') + '\n')
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
