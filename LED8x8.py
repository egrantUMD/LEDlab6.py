import RPi.GPIO as GPIO
from time import sleep
from shifterr import Shifter
import mulitprocessing

GPIO.setmode(GPIO.BCM)

pins = [23, 24, 25]
for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial=0)


class LED8x8:
  pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]

  row = [0b10000000, 0b01000000, 0b00100000, 0b00010000, 0b00001000, 0b00000100, 0b00000010, 0b00000001]

  dataPin, latchPin, clockPin = 23, 24, 25
  
 
  def __init__(self):
    self.shift = Shifter(self.dataPin, self.latchPin, self.clockPin)
  
  def display(self):
    try:
      while True:
        for a in range(8):
          self.shift.shiftByte(~(self.pattern[a] & 0b11111111))
          self.shift.shiftByte(self.row[a])
          self.shift.ping(self.latchPin)
        sleep(0.001)
    except KeyboardInterrupt:
      pass
 
a = LED8x8()
a.display