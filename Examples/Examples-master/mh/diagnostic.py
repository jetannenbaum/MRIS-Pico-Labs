from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import framebuf
import machine
import time
 
xAxis = ADC(Pin(27))
yAxis = ADC(Pin(28))
button = Pin(14,Pin.IN, Pin.PULL_UP)

led1 = Pin(17, Pin.OUT)
led2 = Pin(16, Pin.OUT)
blue_button = Pin(15, Pin.IN, Pin.PULL_DOWN)
 
WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height
 
i2c = I2C(0, scl=Pin(13), sda=Pin(12), freq=200000)       # Init I2C using pins GP8 & GP9 (default I2C0 pins)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config
 
 
oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display
 
# Raspberry Pi logo as 32x32 bytearray
buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
 
while True:
    if blue_button.value():
       if led1.value() == 1:
         led1.low()
         led2.high()
       else:
         led1.high()
         led2.low()
         
       time.sleep(0.1)

    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value()
    
    # Load the raspberry pi logo into the framebuffer (the image is 32x32)
    fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)
 
    # Clear the oled display in case it has junk on it.
    oled.fill(0)
 
    # Blit the image from the framebuffer to the oled display
    oled.blit(fb, 96, 0)
       
    # Joystick status
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
    
    # Add some text
    oled.text("DIAGNOSTIC",0,0)
    
    # Add some text
    oled.text("Button: ", 0,9)
    oled.text(str(blue_button.value()),55, 9)
    
    # Add some text
    oled.text("Leds: ", 0,16)
    oled.text(str(led1.value()),55, 16)
    oled.text(str(led2.value()),65, 16)
    
    #
    oled.text("xAxis: ",0,25)
    #oled.text(str(round(xValue,2)),60,8)
    oled.text(str(xStatus),55,25)
    oled.text("yAxis: ",0,34)
    #oled.text(str(round(yValue,2)),60,17)
    oled.text(str(yStatus),55,34)
    oled.text("Button: ",0,43)
    #oled.text(str(round(yValue,2)),60,17)
    oled.text(str(buttonStatus),55,43)
  
    # Finally update the oled display so the image & text is displayed
    oled.show()
    
    #
    time.sleep(0.1)
