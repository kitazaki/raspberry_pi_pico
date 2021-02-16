import machine
import utime
led1 = machine.Pin(25, machine.Pin.OUT)
led1.value(0)
led2 = machine.Pin(2, machine.Pin.OUT)
while True:
  led2.value(1)
  utime.sleep(1)
  led2.value(0)
  utime.sleep(1)