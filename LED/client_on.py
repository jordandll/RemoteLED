#!/usr/bin/python3

import socket as sock

sock.setdefaulttimeout(2)

# Control codes.

LED_ON=b'\x01'
LED_OFF=b'\x00'
LED_CHECK=b'\x10'

# Common error messages specific to sockets.
err_msg_timeout='Connection Error:\tConnection timeout error occurred with server at \'{0}\' listening on port {1:d}.'

# Create client socket, denoted as 's'.
s = sock.socket()


# Parse the command line for address info.
import sys
argv = sys.argv

if '-h' in argv:
    HOST = argv[argv.index('-h')+1]
elif '--host' in argv:
    HOST = argv[argv.index('--host')+1]
else:
    HOST = '127.0.0.1'

if '-p' in argv:
    PORT = int(argv[argv.index('-p')+1])
elif '--port' in argv:
    PORT = int(argv[argv.index('--port')+1])
else:
    PORT = 9001

ADDR=(HOST, PORT)

# Connect to server at HOST listening on port PORT.
try:
    s.connect(ADDR)
except sock.timeout:
    print(err_msg_timeout.format(*ADDR))
    exit(1)

# Send 'LED on' command to the server and wait for server response that merely indicates that the command was received.
# An error here simply implies a connectivity issue as opposed to an error with command itself.

sent=s.send(LED_ON)
print(f'Client sent {sent:d} bytes of data to \'s://{HOST}:{PORT:d}/\'.')

try:
    msg_r=s.recv(1024)
except sock.timeout:
    print(err_msg_timeout.format(*ADDR))
    exit(1)

print('Server received the command.')


# Wait for follow up response from the server indicating success/error with the command itself.
try:
    msg_r=s.recv(1024)
except sock.timeout:
    print(err_msg_timeout.format(*ADDR))
    exit(1)

print('The server sent:  \'' + str(msg_r, 'utf-8') + '\'.')

# Close and disconnect.
s.close()



