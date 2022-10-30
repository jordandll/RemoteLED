from gpiozero import MotionSensor
from signal import pause


def on_msg():
    print('Motion sensor ON.')


def off_msg():
    print('Motion sensor OFF.')


pir = MotionSensor(pin=7, pull_up=True, queue_len=5)

pir.when_activated = on_msg
pir.when_deactivated = off_msg

try:
    pause()
except KeyboardInterrupt:
    print('Keyboard interrupt received.  Stopping script.')
