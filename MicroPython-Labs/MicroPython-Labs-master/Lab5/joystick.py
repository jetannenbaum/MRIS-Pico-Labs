from machine import Pin, ADC
import time

xAxis = ADC(Pin(27))
yAxis = ADC(Pin(28))
button = Pin(14,Pin.IN, Pin.PULL_UP)

while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value()
    xStatus = "middle"
    yStatus = "middle"
    buttonStatus = "not pressed"
    if xValue <= 600:
        xStatus = "up"
    elif xValue >= 60000:
        xStatus = "down"
    if yValue <= 600:
        yStatus = "right"
    elif yValue >= 60000:
        yStatus = "left"
    if buttonValue == 0:
        buttonStatus = "pressed"
    print("X: " + xStatus + ", Y: " + yStatus + " -- button " + buttonStatus)
    time.sleep(0.1)
