from machine import Pin
from utime import sleep

print("Hello, Pi Pico!")

led = Pin(25, Pin.OUT)
while True:
  led.toggle()
  sleep(0.5)