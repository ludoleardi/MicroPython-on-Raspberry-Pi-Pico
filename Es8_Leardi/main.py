import machine
import utime

from machine import Pin

potentiometer = machine.ADC(28)
led = Pin(5, Pin.OUT)

conversion_factor = 3.3 / (65535)

while True:
  duty_cicle = (potentiometer.read_u16() * conversion_factor) /3.3
  ta = (int) (duty_cicle / 100)
  ts = (int) ((1 - duty_cicle) / 100)
  led.value(1)
  utime.sleep(ta)
  led.value(0)
  utime.sleep(ts)