#!/usr/bin/python3
import socket as sock
from datetime import datetime

# TODO:  Write code to parse the command line arguments for '--host' or '-h' and ...
# ... '--port' or '-p' options.  Assuming they are found, set the 'HOST' and 'PORT' ...
# ... variables accordingly.

# Address Info.
HOST = '127.0.0.1'
PORT = 9001
ADDR = (HOST, PORT)

# Create server socket bound to HOST and listening on port PORT.
ss = sock.socket()
ss.bind(ADDR)
ss.listen(5)

# Begin main server loop.
try:
    while True:
    # Accept new connections.
        s, addr = ss.accept()
        s.settimeout(2)
    # Receive message.
        try:
            msg = s.recv(1024)
        except sock.timeout:
            print(f'ERROR {str(datetime.today())[:-3]}:\tConnection timeout error occurred with client \'{addr[0]}:{addr[1]:d}\'.') 
            s.close()
            continue
    # Reflect message back to client.
        sent = s.send(msg)
    # Print message from client.
        smsg = str(msg, encoding='utf-8')
        print(f'{str(datetime.today())[:-3]}:\tClient \'{addr[0]}:{addr[1]:d}\' sent message \'{smsg}\'.')
    # Cleanup
        s.close()
except KeyboardInterrupt:
    print('Server stopped by keyboard interrupt.')
    s.close(); ss.close()
    exit(0)
except Exception as e:
    print(e)
    s.close(); ss.close()
    exit(1)
