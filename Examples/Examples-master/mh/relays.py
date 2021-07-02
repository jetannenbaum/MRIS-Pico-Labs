from machine import Pin
import utime

relay1 = Pin(20, Pin.OUT)
relay1.high()
relay2 = Pin(21, Pin.OUT)
relay2.low()


while True:
    # Toggle one relay on and one relay off, for no perticular reason 
    relay1.toggle()
    relay2.toggle()
    utime.sleep(1)
    
