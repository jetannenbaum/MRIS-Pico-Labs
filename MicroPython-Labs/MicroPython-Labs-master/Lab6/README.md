## OLED Display - Driven from the Joystick inputs 

In this lab we want to show the joustick position data on the tiny screen. 

---

We will be adding a SSD1306 OLED I2C display. The I2C is a type of serial device that can be chained together up to 127 devices on the same connection (not that I would recommend it). 

![OLED Display](https://github.optum.com/MRIS-Pico-Labs/Labs/blob/master/Lab6/pico_display_joystick_adc.png)

This shows my configuration but shows a few extras that are not connected because I was checking the space.  

For this you will need to connect SDA to pin 17 (GPIO-13), SCL to pin 16 (GPIO-12), vcc to +ve power rail top of board and   GND to PIN 16 

You also will need to save the SSD1306.py library to your Pico.

<img src="https://github.optum.com/MRIS-Pico-Labs/Labs/blob/master/Lab6/Lab6.png" width="600">

The program for this is a little more complicated so I recommend you save and run oled.py. Joystick actions should show on the OLED display. 

Your display has 16 vertical pixels of yellow, one pixel of dead space, 48 pixels of blue. The one color displays are solid but I didn't know at time of ordering. 

### Extra credit: Write your own text or draw your own shapes to the display
