import libclient as lc
from gpiozero import MotionSensor
from signal import pause

on_msg = lc.gen_send_msg('Motion ON.')
off_msg = lc.gen_send_msg('Motion OFF.')

pir = MotionSensor(pin=7, pull_up=True, queue_len=5)

pir.when_motion = on_msg
pir.when_no_motion = off_msg

pause()
