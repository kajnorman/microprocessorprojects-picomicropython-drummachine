from machine import Pin
from time import sleep


l1 = Pin(16,Pin.OUT)


l1.on()

sleep(0.6)


l1.off()
