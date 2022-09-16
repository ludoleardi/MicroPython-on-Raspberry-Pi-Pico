import machine
import utime

conversion_factor = 3.3 / (65535)

print("Lettura tensione pin 28\n")

potentiometer = machine.ADC(28)

while True:
  reading = potentiometer.read_u16() * conversion_factor
  print(reading)
  utime.sleep(1)
