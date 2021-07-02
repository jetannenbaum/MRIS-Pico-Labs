import time
from machine import Pin, I2C
from VL53L0X import VL53L0X
from ssd1306 import SSD1306_I2C

print("setting up i2c")
i2cToF = I2C(1, sda=Pin(2), scl=Pin(3), freq=400000)
i2cDisplay=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)

print("creating vl53lox object")
tof = VL53L0X(i2cToF)

print("creating display object")
oled = SSD1306_I2C(128, 64, i2cDisplay)

print("getting and displaying range")
while True:
    oled.fill(0)

    # Start ranging
    measureMM = tof.ping() - 25
    oled.text(str(measureMM) + " mm", 0, 0)
    measureIn = round(measureMM / 25.4, 2)
    oled.text(str(measureIn) + " inches", 0, 10)
    oled.show()
    time.sleep(.25)
