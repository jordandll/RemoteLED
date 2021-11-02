#!/usr/bin/python3

import socket as sock
import subprocess

sock.setdefaulttimeout(2)

# Control codes.
LED_ON=b'\x01'
LED_OFF=b'\x00'
LED_CHECK=b'\x10'

# Common error messages specific to sockets.
err_msg_timeout='Connection Error:\tConnection timeout error occurred with client at \'{0}\' on port {1:d}.'

# Create a server at 'localhost' listening on port 9001.
HOST='127.0.0.1'
PORT=9001
ADDR=(HOST, PORT)
ss=sock.socket()
ss.bind(ADDR)

# Accept incoming connection by listening on port 9001.
try:
    s, addr = ss.accept()
except KeyboardInterrupt:
    print('\nServer was stopped by a keyboard interrupt before a connection was accepted.')
    exit(0)
    
# Wait for a command to be sent.
try:
    msg_r=s.recv(1024)
except sock.timeout:
    print(err_msg_timeout.format(*addr))
    exit(1)

# Simply notify the client that the command was received.
sent=s.send(b'\x01')
print(f'Server sent {sent:d} bytes of data to \'{addr[0]}:{addr[1]:d}\'.')

# Check control code.
cmd = msg_r[0]
if cmd == 2:
    # Check LED command not implemented yet.
    sent=s.send(b'Check LED command not implemented yet.')
    print(f'Server sent {sent:d} bytes of data to \'{addr[0]}:{addr[1]:d}\'.')
    s.close()
    ss.close()
    exit(0)
elif cmd != 1 and cmd != 0:
    # Invalid control code.
    sent=s.send(b'Invalid control code.')
    print(f'Server sent {sent:d} bytes of data to \'{addr[0]}:{addr[1]:d}\'.')
    s.close()
    ss.close()
    exit(0)

# Now execute the command and send the results to the client.
run = subprocess.run
if cmd == 0:
    comp_proc = run(['python3', '2_off.py'], stdout=subprocess.PIPE)
else:
    comp_proc = run(['python3', '2_on.py'], stdout=subprocess.PIPE)

print('Command \'{0}\' returned a value of {1:d}.'.format(comp_proc.args[0] + ' ' + comp_proc.args[1], comp_proc.returncode))
sent=s.send(comp_proc.stdout)
print(f'Server sent {sent:d} bytes of data to \'{addr[0]}:{addr[1]:d}\'.')

# Close and disconnect.
s.close()
ss.close()
