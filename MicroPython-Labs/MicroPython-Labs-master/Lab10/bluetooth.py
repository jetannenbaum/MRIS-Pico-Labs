from machine import Pin, UART

def readUartBytes(uart):
    resp = b""
    if uart.any():
        resp = b"".join([resp, uart.read(1)])
    return (resp.decode())
 
# Create the UART
uart1 = UART(id=1, baudrate=9600, tx=Pin(4), rx=Pin(5))

# Loop
while True:
    data = str(readUartBytes(uart1)).lower()
    if data != "":
        print(data)