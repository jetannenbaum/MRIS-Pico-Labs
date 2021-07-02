This application allows a user to read and write to the HM-10 blue tooth modules at different baud rates on different UARTs.

UART0 is set to 115200 baud and UART1 is set to 9600 baud

Different modules have different baud rates, depending on the software version

Commands are prefixed by the uart port (0 for UART0, 1 for UART1, and 2 for both)

The code is loosely based on code that I found on the SMARSFAN youtube channel.

I can connect to the modules now, but haven't figured out how to read from (or write to) the blue tooth serial terminal on my phone

Scratch that, I can connect to the modules from my phone and I can have them talk to each other.   I use LightBlue on my iPhone to talk
to the modules.  Works better than the other app I used which didn't work properly.

A few helpful notes:
1. Note all HM-10 modules are created equal.  I bought cheap ones. 

      a. They had different software revisions and thus required different baud rates to talk to the UARTS.  
              By default, the baud rate is supposed to be 9600 baud.
              
      b. Not all HM-10 modules require \r\n to terminate the command.  Once again, cheap clone required it.
      
      c. When connecting bluetooth modules together, beware of other bluetooth emitters.  I hade to make sure I was connecting
         to the module I wanted, not some random bluetooth device in the house.  Use AT+LADDR to find the address of your device,
         then AT+INQ to scan for it before trying to connect.  Otherwise, you might connect to your fitbit :-)
         
      d. The UART to bluetooth module baud rate doesn't matter when communicating between bluettoth modules.  I have two modules,
         one set at 9600 baud and the other at 115200.
         
      e. uart.read vs. uart.readline - this gave me some trouble, since I didn't always get a clean response using uart.readline.
         I suspect it mostly depends on what you send to the module.  If every command is terminated by \r\n, then use uart.readline.
         
 2. Just played with the "official" HM-10 module from DSD Tech. 
      a. These modules do not require the \r\n after a command.  While the documentation says they will accept it, it does not appear to          be the case.
      
      b. Query commands, such as AT+ROLE require a question mark (?) after the command.
      
      c. On the plus side, they link together very easily.  I had two connected and made one the master.  It immediately linked to the
         second module.  On the down side, I had to remove power from the slaved module before I could change the role on the master.
         
      d.  Don't bother with the AT+HELP? command.  It links back to the OEM site for the module.
