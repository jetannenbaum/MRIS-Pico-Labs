from machine import Pin, Timer

# LED - dark
led1 = Pin(17, Pin.OUT) 
led1.low()

# LED - light
led2 = Pin(16, Pin.OUT)
led2.high()

tim = Timer()

# First function and we are using globals to provide led variable access
def tick(timer):
  global led1
  led1.toggle()
  global led2
  led2.toggle()
  
tim.init(freq = 5, mode=Timer.PERIODIC, callback=tick)
