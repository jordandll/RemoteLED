#!/usr/bin/python3

import socket as sock
import subprocess
from signal import SIGINT

"""Herein is a list of python scripts (commands), each with an index that is equal to it's control code. """
tree_cmd = ['all_on.py', 'alt.py', 'ants.py']

# Common error messages specific to sockets.
err_msg_timeout = 'Connection Error:\tConnection timeout error occurred with client at \'{0}\' on port {1:d}.'

# Parse the command line for address info.
import sys

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

# Create server socket bound to HOST listening on port PORT.
ss = sock.socket()
ss.bind(ADDR)
ss.listen(1)


# Defined special pseudo super class of subprocess.Popen to avoid a NameError below.
class SuperPopen:
    """This is a pseudo super class of subprocess.Popen"""
    def __init__(self):
        self.returncode = 0


# Define shorthand references for subprocess elements.
Popen = subprocess.Popen

# This symbol will later be redefined as a Popen object.
p = SuperPopen()

while True:
    # Accept incoming connection by listening on port 9001.
    try:
        s, addr = ss.accept()
    except KeyboardInterrupt:
        print('\nServer was stopped by a keyboard interrupt before a connection was accepted.')
        exit(0)

    sock.setdefaulttimeout(2)

    # Wait for a command to be sent.
    try:
        msg_r = s.recv(1024)
    except sock.timeout:
        print(err_msg_timeout.format(*addr))
        exit(1)

    # Simply notify the client that the command was received.
    # sent=s.send(b'\x01')
    sent = 0
    print(f'Server sent {sent:d} bytes of data to \'{addr[0]}:{addr[1]:d}\'.')

    # Store control code.
    code = msg_r[0]

    # Check the state of the child process that is executing the tree command, denoted as 'p'.
    if p.returncode is None:
        """The process is still running."""
        p.send_signal(SIGINT)
        p.wait(1)
        # TODO:  Check if we need to kill the process as well.
        if code != 0:
            p = Popen(['python3', tree_cmd[code - 1]], stdout=subprocess.PIPE, encoding='utf-8')
    elif code != 0:
        """The process is not currently active (running)."""
        p = Popen(['python3', tree_cmd[code - 1]], stdout=subprocess.PIPE, encoding='utf-8')

    s.close()

ss.close()
