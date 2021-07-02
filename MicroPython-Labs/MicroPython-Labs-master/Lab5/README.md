## Lab 5 - Joystick 2-axis ADC input and push button

In this lab we will add a 2 axis joystick. This is just 2 ADC analogue inputs and the model you have also has a push down that is a button. 

---

![Pico pinout](https://cdn.mos.cms.futurecdn.net/NF4vsRaVqecVwjpmX8Cj8n-970-80.png)

We are now going to use our second breadboard and add the 2 axis joystick.  This has 5 liness button (press down) X and Y where the X and Y are analogue inputs (potentiometers give a variable voltage), the position can be determined using 2 ADC lines. 

This looks more complicatted than it really is.  The joystick control has 5 pins and you should have a 5 wire F-M cable connect these together.   The joystick does not pin down so it will move around.  The pins on the joystick are 

```
SW VRY VRX +5v GND

SW = Switch or push
VRY = Variable Resistor Y 
VRX = Variable Resistor X
+5v = +ve (positive actually 3.3v for us)
GRD = -ve (ground) 
```

<img src="https://github.optum.com/MRIS-Pico-Labs/Labs/blob/master/Lab5/Lab5.png" width="600">

I wired the switch into pin 19 (GPIO-14, not an ADC),  Y-axis into pin 34 (ADC-2), X-axis into pin 32 (ADC-1), positive into the top rail and -ve into pin 3 or GND (any of the black ones on the pinout diagram will work). 

If you want to code it yourself please read https://www.tomshardware.com/how-to/raspberry-pi-pico-joystick or save/run the joystick.py program. You should get X, Y and Press position in the output console. 

```
X: down, Y: right -- button not pressed
X: down, Y: right -- button not pressed
X: middle, Y: middle -- button not pressed
X: middle, Y: middle -- button not pressed
X: middle, Y: middle -- button not pressed
X: middle, Y: middle -- button not pressed
X: middle, Y: middle -- button not pressed
X: middle, Y: right -- button not pressed
X: down, Y: right -- button not pressed
X: down, Y: middle -- button not pressed
X: down, Y: middle -- button not pressed
X: down, Y: left -- button not pressed
X: middle, Y: left -- button not pressed
X: middle, Y: middle -- button not pressed
X: middle, Y: right -- button not pressed
X: down, Y: right -- button not pressed
X: down, Y: middle -- button not pressed
X: down, Y: left -- button not pressed
X: middle, Y: middle -- button not pressed
X: middle, Y: middle -- button pressed
X: middle, Y: middle -- button pressed
```

#### Extra Credit: Use your LEDs to indicate which way the joystick is pointing (right or left). Warning: I did not do this myself so I don't have the answer. 


