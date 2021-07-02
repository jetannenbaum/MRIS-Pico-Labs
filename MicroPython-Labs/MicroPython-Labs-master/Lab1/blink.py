from machine import Pin
import utime

# Pin 25 is connected to the on board LED
led1 = Pin(25, Pin.OUT)
led1.low()

# Never ending while loop
while True:
  led1.toggle()
  print("Toggle")
  utime.sleep(1)

