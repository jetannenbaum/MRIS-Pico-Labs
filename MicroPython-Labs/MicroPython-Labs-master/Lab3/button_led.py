from machine import Pin
import time

led = Pin(16, Pin.OUT)
button = Pin(15, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value():
        led.toggle()
        print("Button press")
        # This is delay to give time to get finger off the button.  It also means the light blinks if there is a bad connection in the button circuit.
        time.sleep(0.5)
