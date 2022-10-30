# RemoteRPi
A suite of tools that provide remote access to certain aspects of a Raspberry Pi and connected peripheral devices.

## RemoteLED
Remotely turn an LED on/off.
### Modules
- client_on.py
- client_off.py
- led_server.py

## Receive Reflect Protocol
This is a protocol that is used by the 'server.py' -- note that the name is likely to change to be more specific -- script/module and is implemented by an improper subset of the 'libclient.py' module.  The function, 'libclient.send_msg', is the implementing function.  The helper function, 'libclient.gen_send_msg', simply returns a parameterless version of 'send_msg'.
### Modules
- server.py
- libclient.py

