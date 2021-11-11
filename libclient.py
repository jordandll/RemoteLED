#!/usr/bin/python3
import socket as sock
from datetime import datetime

# Default remote socket address.
HOST = '127.0.0.1'
PORT = 9001
ADDR = (HOST, PORT)

sock.setdefaulttimeout(2)

def send_msg(msg: str, addr = ADDR):
# Create client socket.
    s = sock.socket()
# Connect to server.
    try:
        s.connect(addr)
    except ConnectionRefusedError:
        print(f'ERROR {str(datetime.today())[:-3]}:\tConnection with server at \'{addr[0]}:{addr[1]:d}\' refused.')
        s.close()
        return

# Send message.
    s_msg = bytes(msg, encoding='utf-8')
    sent = s.send(s_msg)
# Receive and test reflection.
    try:
        r_msg = s.recv(1024)
    except sock.timeout:
        print(f'ERROR {str(datetime.today())[:-3]}:\tConnection timeout error.')
        s.close()
        return
    if r_msg != s_msg:
        print(f'ERROR {str(datetime.today())[:-3]}:\tReflected message does not match sent message.')
        s.close()
        return
# Log said message.
    print(str(datetime.today())[:-3] + ':\t' + msg)
    s.close()
    
def gen_send_msg(g_msg: str, g_addr = ADDR):
    return lambda: send_msg(g_msg, g_addr)
