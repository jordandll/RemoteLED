from gpiozero import MotionSensor
from signal import pause
import subprocess as sp


def send_msg():
    args = ['python3', 'client.py', 'blink']
    cp = sp.run(args, capture_output=True, encoding='utf-8')
    if cp.stdout is not None:
        print(args[0] + ' ' + args[1] + ' ' + args[2] + ':\t' + cp.stdout)


pir = MotionSensor(pin=7, pull_up=True, queue_len=5)
pir.when_activated = send_msg

try:
    pause()
except KeyboardInterrupt:
    print("\nKeyboard interrupt received.  Stopping script.")
