from machine import Pin, I2C
from vl53l0x import VL53L0X
import time # sleep

i2cToF = I2C(1, sda=Pin(2), scl=Pin(3), freq=400000)
tof = VL53L0X(i2cToF)

while True:
    measureMM = tof.ping() - 25
    measureIn = round(measureMM / 25.4, 2)
    print("Distance: " + str(measureIn) + " inches")
