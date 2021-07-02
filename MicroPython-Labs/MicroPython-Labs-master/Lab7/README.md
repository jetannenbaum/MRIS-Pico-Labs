## Lab 7 - Generates a tone using PWM (Pulse Width Modulation)

In this lab we will add sound using a PWM or Piezo module.  Don't expect a lot these don't have much tone or volume.  

---

<img src="https://github.optum.com/MRIS-Pico-Labs/Labs/blob/master/Lab7/Lab7.png" width="600">

Add your PWM Piezo buzzer to your breadboard. I believe there is an orientation so if it doesn't work try rotating it 180 degrees. Connect the positive side to pin 15 (GPIO-11) and the other side to any ground but pin 13 is shown in the diagram. 

To make a tone we occolate at a given frequency and amplitude, this gives our tone and volume. The code provided in tone.py will make an initial single note.  Copy it onto the Pico and run it. This is mostly confirm the sound curcuit is working. 

I found a more musical option at https://github.com/james1236/buzzer_music if you add buzzer_music.py and song.py to your Pico you can then choose a tune.  The buzzer_music.py is a reuseable note library with the full scale of possible notes and the song.py have the musical compositions. I have it on Tetris, you will run song.py.  

Try making your own tune and playing it. 

I made 
```
    # Mike's song - Time, Note, Duration, Instrument - I think our instrument is always 0 unless you add a second PWM piezo. 
    song = "0 A4 1 0;2 A2 1 0;4 A3 1 0;6 A1 1 0"
```
---

Alternative ways to connect a sound device 
There are several different ways that you can connect a sound device to your MicroController. Here are three options:

Buzzers - These are small inexpensive devices that can mount directly on your breadboard.
Piezoelectric Speaker - Wikipedia Page on Piezoelectric Speaker
Speaker - A magnetic speaker with our without an amplifier is another way to hear sound. You can also purchase a small amplifier to increase the volume.
Amplifier - For about $1.20 you can purchase a small amplifier for your speaker. eBay LM386 DC 5V-12V Mini Micro Audio Amplifier Module Board
 

References
https://electronics.stackexchange.com/questions/288930/what-is-the-difference-between-a-buzzer-and-a-speaker-and-are-there-any-other-ba
https://www.coderdojotc.org/micropython/sound/01-intro/

### Extra credit: Make some tones and play your own tune.   You were provided a second PWM they to play a cord (2 notes at the same time),
