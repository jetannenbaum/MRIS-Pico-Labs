## Lab 4 - Analog to Digital Conversion (ADC) using the on-board temperature sensor

In this lab you will read a variable voltage that represents the temporature range of the processor. No wiring for this one. 

---

This lab uses one of the ADC, the CPU has an in built temperature sensor. The ADC will give a number from 0 - 65535. This is shown as a variable voltage from 0 to 3.3 volts.  

We will just use ADC(4).  You can read more at https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/8 this example is an external analogue input so ours will need to use the internal one, or you can load and run the adc.py

Output will give the CPU temperature in Celsius and Fahrenheit. If you warm the CPU with your finger you can see it start to go up (it should not be too hot to touch but maybe check the output first before you do).
```
MicroPython v1.15 on 2021-04-18; Raspberry Pi Pico with RP2040
Type "help()" for more information.
>>> %Run -c $EDITOR_CONTENT
C: 20.02224 F: 68.04003
C: 19.55409 F: 67.19738
C: 19.55409 F: 67.19738
C: 20.02224 F: 68.04003
C: 19.55409 F: 67.19738
C: 19.08595 F: 66.35471
C: 20.02224 F: 68.04003
C: 19.08595 F: 66.35471
C: 19.55409 F: 67.19738
C: 20.02224 F: 68.04003
C: 20.02224 F: 68.04003
C: 20.02224 F: 68.04003
C: 19.55409 F: 67.19738
```

#### Extra Credit: Round the decimals to only 1 decimal place, some google hunting is required. 
