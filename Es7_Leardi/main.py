import machine
import utime

from machine import Pin

led = Pin(5, Pin.OUT)

duty_cicle = 0.5
ta = (int) (duty_cicle / 100)
ts = (int) ((1 - duty_cicle) / 100)

while True:
  led.value(1)
  utime.sleep(ta)
  led.value(0)
  utime.sleep(ts)