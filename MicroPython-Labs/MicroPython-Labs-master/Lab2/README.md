## Lab 2 - Strobe between onboard LED and your LED 

In this lab you will add additional external LEDs, add connections for ground and power, and then make them flash.

---

Reference content for this Lab came from 
* If you want to know more pleasse read this https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/6
* An alternative option for the same first steps is at https://www.tomshardware.com/how-to/raspberry-pi-pico-setup

Each pin on the Pico has a purpose and several can do more than one depending on what we specify in the code. Once wired we will only use the pin for the one purpose we have decided 

Note: I hope we will not need to move any because we need a specific pin but we will find out with time

![Pico pinout](https://cdn.mos.cms.futurecdn.net/NF4vsRaVqecVwjpmX8Cj8n-970-80.png)

We will connect ground pin 38 using a resistor to -ve, then connect LEDs to pin 22 (light green General Purpose Input/Output or GPIO-17), and pin 21 (GPIO-16). LEDs will need to be in the correct orientation to light (the shorter leg is usually the negative and the longer one the positive)

<img src="https://github.optum.com/MRIS-Pico-Labs/Labs/blob/master/Lab2/Lab2.png" width="600">

You can now modify the blink code to use the new pins or copy the strobe.py. Save it to the Pico and run. Again you may need to choose stop if you are told the Pico is busy. 

#### Extra Credit: Connect up more LEDs on other GPIO lines and have them flash too
