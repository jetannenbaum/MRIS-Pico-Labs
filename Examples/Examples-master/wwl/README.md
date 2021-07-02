# Pico Hygrometer
<hr>

This is still work in progress.

If you would like to try it out you will need
two components.

 [DHT11 Sensor](https://www.amazon.com/Temperature-Humidity-Digital-3-3V-5V-Raspberry/dp/B07WT2HJ4F/ref=sr_1_5?crid=L4IDDTOPM1A9&dchild=1&keywords=dht11+sensor&qid=1624639813&sprefix=dht11%2Caps%2C229&sr=8-5)
7 male to female jumper wires.
 [16x2 LCD Display](https://www.amazon.com/SunFounder-Serial-Module-Display-Arduino/dp/B019K5X53O/ref=sr_1_1_sspa?dchild=1&keywords=16x2+LCD&qid=1624639684&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExQUNLQUlOVVE2OEU5JmVuY3J5cHRlZElkPUEwNTkyNzExMkFRV1I3SDhFQ1k3NiZlbmNyeXB0ZWRBZElkPUEwNjg1NDY1M0hTTDVSTVhZQlNUQyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=)


Software:

Put the lib directory and it contents on your Pico,
you can use Thonny to create the lib directory. Put the remaining files in the same directory where you created lib.

Wiring Layout:

pin 0 to sda on LCD Display
pin 1 to scl on LCD Display
pin 3 to Ground on LCD Display
Pin 40 to VCC on LCD Display

Pin 40 to VCC on DHT11
Pin 38 to ground on DHT11
Pin 21 to to Data

I will update with better documentation when project is complete.

weather-station.py is the main program.
