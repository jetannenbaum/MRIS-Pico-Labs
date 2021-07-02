from machine import ADC
import time

temp_sensor = ADC(4)

while True:
  temperature = temp_sensor.read_u16()

  to_volts = 3.3 / 65535
  temperature = temperature * to_volts

  celsius_degrees = 27 - (temperature - 0.706) / 0.001721
  fahrenheit_degrees = celsius_degrees * 9 / 5 + 32
  print("C: " + str(celsius_degrees) + " F: " + str(fahrenheit_degrees))
  
  time.sleep(1)
