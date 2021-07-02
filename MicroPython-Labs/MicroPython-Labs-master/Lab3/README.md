## Lab 3 - Button Input to toggle LED output lights

In this lab we will add an external input button that can be used to change the state of the LEDs.

---

![Pico pinout](https://cdn.mos.cms.futurecdn.net/NF4vsRaVqecVwjpmX8Cj8n-970-80.png)

Connect the 3.3v out PIN 34 to the +ve line, then connect the posivive to one corner of the button, and the opposite corner to the PIN 20 or GPIO 15. There may be some experimentation required depending on the orientation of the button but oppisite corners should work. 

This is a pull down circuit (meaning there is no voltage until you press the button, a pull up has power until you press the button). It starts low (0 - no power) and then goes high (1 - yes power) when you press the button. 

<img src="https://github.optum.com/MRIS-Pico-Labs/Labs/blob/master/Lab3/Lab3.png" width="600">

You can read up how to configure an input pin (button = Pin(15, Pin.IN, Pin.PULL_DOWN), more readiing here https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/6 or load/run the button_led.py

if you press the button it should change the LED state but if you don't take your finger off the button it will blink every half second (500ms) because this is how often we check the button state. 

#### Extra Credit: Use the button to turn one LED off when you turn the other on.
