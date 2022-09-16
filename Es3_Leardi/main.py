from machine import Pin
from utime import sleep

print("Hello, Pi Pico!")

red = Pin(5, Pin.OUT)
yellow = Pin(4, Pin.OUT)
green = Pin(3, Pin.OUT)

red.value(0)
yellow.value(0)
green.value(0)

while True:
  red.toggle()
  sleep(5)
  red.toggle()
  green.toggle()
  sleep(5)
  green.toggle()
  yellow.toggle()
  sleep(5)
  yellow.toggle()