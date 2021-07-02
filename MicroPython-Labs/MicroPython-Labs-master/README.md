# Training Labs
This innovation and skills development program is going to progressively going to work from simple to harder labs. No prior knowledge of coding, Python, and electronics is not required.  The assignments will go from simple output, simple input, and we will build to making a game that you control with the joystick or buttons. 

You will need a parts kit (we have 18 of them available from Mike, or you can order your own), a usb-a to micro-usb cable, and a computer for writing/testing the code.  At the end of the program you are welcome to keep your kit but if you want to give it back to avoid e-waste then we will gift them to a kids STEM program.

## Parts kit

> The parts kit contains
> - 1 x Raspberry Pi Pico microcontrollor board (with soldered headers thanks to Rachael and JET)
> - 2 x 400 prototyping breadboards (some kits may have a 1 x 830 larger breadboard)
> - 1 x 0.96 inch OLED display SSD1306 I2C 128x64 - two color yellow and blue (top part yellow, the rest blue, not under your control) 
> - 1 x 2 axis joystick 
> - 1 x Analogue input - Potentiometer variable resistor and knob
> - 4 x LEDs of different colors
> - 3 x 220 - 330 ohm resistors 
> - 2 x PWM Piezo speakers - 160ohm passive 3-5v speaker(s) - I think you will only need 1 but I put 2 if anyone wants to get creative with stereo
> - 4 x Miniature botton presses
> - 1 x 4 M-F connector cable (for the screen) - I ended up using the M-M cables so I could put my screen in the board.
> - 1 x 5 M-F connector cable (for the joystick)
> - Assorted M-M connector cables
> - Plastic Box
> - 2 x Light Dependent Resistors (5528) will be added to kits but people who were early adopters should ask for them
Other parts and cables are available if you need them, so just ask. 

## IDE Set up

There are two main choices for the development IDE
* Thonny IDE (https://thonny.org) which is easy to use but is not approved in the App.Store
* Microsoft Visual Studio Code IDE (https://code.visualstudio.com) which is approved (https://optum.service-now.com/euts_intake?id=euts_appstore_app_details&appKeyId=27353 this was the latest version at time of writing). You will need to add the Pico-Go extension

#### Use of UHC equipement to image the firmware has proven difficult because USB flash drive write has been disabled. Your firmware is already written and development uses serial comminication so it should be ok.   

## Getting Started

Take one of the breadboards and insert your pico lined up along the center groove. This groove it to help get under the board if you need to move or remove it.  If you line up starting at 1 on the breadboard this may help you in finding the right pins later. 

If you need to load firmware you can press the white button while powering up but we did this for you because of the UHC limitations. 

Plug in your USB cable to power up and you should be able to connect in the IDE: 
* Thonny: Hit the stop/reconnect button if the lower panel does not give a prompt. If that does not work, make sure the lower right corner of the application says 'MicroPython (Raspberry Pi Pico).' To change that, simply click the dialog and switch it over. 
* Visual Studio Code: The Pico should automatically connect to the comm port.  The terminal window should say "Connecting to COMx..." 
*     Then look at the bottom left of the screen.  It should say "Pico Connected"-  If it says "Pico Disconnected" 
*     click on the words and the board should connect.
* NOTE: If the Pico is not connecting, try various USB Cables. 

<Add Screen Shot>
  
We should now be able to write python test commands to check the pico is working and the firmware update was successful. 

In the console window of your IDE at the prompt (">>>") put 
```
> print("Hello World")
```

hit return, you should see 
```
    Hello World
```
Congratulations you have written and executed your first embedded Python command.



