## Wayne 2021

import utime
import machine 
from machine import I2C,ADC,Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from dht import DHT11, InvalidChecksum
import time
import _thread

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 15

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)  

led1 = Pin(12, Pin.OUT)
led2 = Pin(13, Pin.OUT)
led3 = Pin(14, Pin.OUT)
led4 = Pin(15, Pin.OUT)
led = Pin(25, Pin.OUT)

baton = _thread.allocate_lock()

pin = Pin(16, Pin.OUT, Pin.PULL_DOWN)
sensor = DHT11(pin)
  
def core_task():
    baton.acquire()
    sensor_temp = ADC(4)
    conversion_factor = 3.3 / (65535)
    led.on()
    baton.release()
    
_thread.start_new_thread(core_task, ())

while True:
    core_task()
    dew = (sensor.temperature * 1.8 + 32-(100-sensor.humidity)/5.0)
    lcd.move_to(0, 0)
    lcd.putstr("Temp: {:.2f}\n".format(sensor.temperature * 1.8 + 32))
    lcd.move_to(0, 1)
    lcd.putstr("H: {}".format(sensor.humidity))
    lcd.move_to(8, 1)
    lcd.putstr("D: {:.1f}".format(dew))
    utime.sleep(2)
    time.sleep(5)
    lcd.clear()
    
