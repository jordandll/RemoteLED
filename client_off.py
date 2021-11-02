#!/usr/bin/python3

import socket as sock

# Common error messages specific to sockets.
err_msg_timeout='Connection Error:\tConnection timeout error occurred with server at \'{0}\' listening on port {1:d}.'

# Connect to server at 'localhost' listening on port 9001.
HOST='127.0.0.1'
PORT=9001
ADDR=(HOST, PORT)
try:
    s.connect(ADDR)
except sock.timeout:
    print(err_msg_timeout.format(*ADDR))
    exit(1)

# Send 'LED off' command to the server and wait for server response that merely indicates that the command was received.
# An error here simply implies a connectivity issue as opposed to an error with command itself.

LED_ON=b'\x01'
LED_OFF=b'\x00'
LED_CHECK=b'\x10'

sent=s.send(LED_OFF)
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



