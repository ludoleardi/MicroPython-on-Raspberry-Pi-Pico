import time, _thread, machine

potentiometer = machine.ADC(28)
conversion_factor = 3.3 / (65535)

def allarme():
  buzzer = machine.Pin(8, machine.Pin.OUT)
  buzzer.value(1)
  sleep(0.5)
  buzzer.value(0)

buzzer = machine.Pin(8, machine.Pin.OUT)
buzzer.value(0);

while True:
  reading = potentiometer.read_u16() * conversion_factor
  if(reading > 3.0):
    _thread.start_new_thread(allarme, ())