#!/usr/bin/python3

import socket as sock
import sys

sock.setdefaulttimeout(2)

# Common error messages specific to sockets.
err_msg_timeout = 'Connection Error:\tConnection timeout error occurred with server at \'{0}\' listening on port {1:d}.'

# Create client socket, denoted as 's'.
s = sock.socket()

# Parse the command line for address info.
argv = sys.argv

if '-h' in argv:
    HOST = argv[argv.index('-h') + 1]
elif '--host' in argv:
    HOST = argv[argv.index('--host') + 1]
else:
    HOST = '127.0.0.1'

if '-p' in argv:
    PORT = int(argv[argv.index('-p') + 1])
elif '--port' in argv:
    PORT = int(argv[argv.index('--port') + 1])
else:
    PORT = 9001

ADDR = (HOST, PORT)

# Obtain the command string from the command line (it must be the last argument).
cmd = argv[-1]

# Connect to server at HOST listening on port PORT.
try:
    s.connect(ADDR)
except sock.timeout:
    print(err_msg_timeout.format(*ADDR))
    exit(1)

sent = s.send(cmd.encode(encoding='utf-8'))

code = 0
if sent != len(cmd):
    print("ERROR:\tThe bytes sent is not equal to the length of the command string.")
    code = 1

print(f'Client sent {sent:d} bytes of data to \'s://{HOST}:{PORT:d}/\'.')

# Close and disconnect.
s.close()

exit(code)
