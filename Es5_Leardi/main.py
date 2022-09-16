from machine import Pin
from utime import sleep

red = Pin(5, Pin.OUT)
yellow = Pin(4, Pin.OUT)
green = Pin(3, Pin.OUT)

button = Pin(12, Pin.IN, Pin.PULL_UP)

while True:
  red.value(0)
  yellow.value(0)
  green.value(0)

  if(button.value() == 0):
    red.toggle()
    sleep(2)
    red.toggle()
    green.toggle()
    sleep(2)
    green.toggle()
    yellow.toggle()
    sleep(2)
    yellow.toggle()
  else:
    yellow.value(1)
    sleep(0.5)
    yellow.value(0)
    sleep(0.5)