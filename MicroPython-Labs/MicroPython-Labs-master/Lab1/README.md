## Lab 1 - Make the on board LED blink once per second

In this lab you will install the Pico onto the breadboard and make the onboard Light Emitting Diode (LED) flash. 

---

Background documentation for all the activities included in the labs can be found at https://github.optum.com/MRIS-Pico-Labs/Pico_Pi_Guide

The breadboard is a solderless way to wire and test electronics, we use the rails to help plug in modules and components and then wire them with jumper cables. 

The -ve rail (set of holes shown here in blue) is generally connected to ground (GND) or 0 volts.

The +ve rail (set of holes shown here in red) is generally connecter to the positive, 3.3v or 5v depending where you connect it.

The other rails (sets of holes shown here in green) will give you a place to connect that connects to the pin (leg) of the Pico.

<img src="https://github.optum.com/MRIS-Pico-Labs/Labs/blob/master/Lab1/Lab1.png" width="625">

Install your Pico by aligned against the end and along the center line. The center line is a groove in case you need to remove components and lets you get under them. I recommend you line up to Pin 1 (leg on the Pico) with the matching numbers on the breadboard.  Some presssure may be required, the pins (legs) should not bend if they are correctly aligned to the holes. 

<img src="https://github.optum.com/MRIS-Pico-Labs/Labs/blob/master/Lab1/Lab1_1.png" width="600">

Now write or copy the blink.py application into your IDE, confirm that you are connected to the Pico and save the code.  In Thonny you will be prompted to save locally or to the Pico.  If you are not prompted check the connection setting in the lower right corner.  Once saved select run (hit the green plan button on Thonny, ??? on MS Code).   If you get a busy message click stop before you hit run. 
