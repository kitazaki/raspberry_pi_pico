import usb_hid
from adafruit_hid.mouse import Mouse
import time
mouse = Mouse(usb_hid.devices)
while True:
    mouse.move(0, 1, 0)
    time.sleep(1)
    mouse.move(0, -1, 0)
    time.sleep(1)
