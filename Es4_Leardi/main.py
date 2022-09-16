from machine import Pin
from utime import sleep

button = Pin(12, Pin.IN, Pin.PULL_UP)
led = Pin(5, Pin.OUT)

led.value(0)

while True:
  if(button.value() == 0):
    led.value(1)
    sleep(0.250)
    led.value(0)