## Lab 9 - Using the second core (Threading) 

In this lab we will put some work on the second tread, I am thinking put the sound for the game on the second core but we will probably need to handle global memory which adds to the fun/challenges.

---

Note: I had to press the stop twice to get both processes to stop before I could deploy new code. 

This is my example of using the second thread, I am hoping you can use the concepts to update your breakout game to put the sound on the second thread.  

GOOD LUCK - Happy Coding

```
from machine import Pin
import time 
import _thread
from buzzer_music import music

button = Pin(15, Pin.IN, Pin.PULL_DOWN)

# Define the function that we will run on the second thread
def second_thread():
    #Mike's song 
    song = "0 A4 1 0;2 A2 1 0;4 A3 1 0;6 A1 1 0"

    #One buzzer on pin 0
    mySong = music(song, pins=[Pin(11)])
    while True:
        # Using a global allows both threads to use the same variable
        global button
        print("Thread 2: Doing something ", button.value())
        if button.value() == 1:
            for x in range(20):
                print(x)
                mySong.tick()
                time.sleep(0.04)
        time.sleep(0.5)
   
# Start the second thread - this will give an error if you already started one   
_thread.start_new_thread(second_thread, ())        

# Original/primary thread
while True:
    print("Thread 1: Doing something")
    time.sleep(0.5)
```


### Extra Credit:  Add a button or potentiometer to turn sounds on/off or adjust the volume. 
