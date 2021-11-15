from random import randint
from shifter import Shifter
from time import sleep


d, l, c = 23, 24, 25

shift = Shifter(d, l, c)
x = 0b00010000
y = 0b00010000
a = 3
b = 3

while True:
  x_move = randint(1,3)
  y_move = randint(1,3)
  if a >=0 and a <= 7:
    if x_move == 1 and a !=0 : #moves -1 place
      x <<=1
      a -=1

    elif x_move == 2 and a !=7: # moves 1 place
      x >>=1
      a+=1

    else: # moves zero place
      pass


  if b >=0 and b <= 7:
    if y_move == 1 and b != 0: #moves -1 place
      y <<=1
      b -=1

    elif y_move == 2 and b != 7: # moves 1 place
      y >>=1
      b+=1

    else: # moves zero place
      pass
  print("{:b} , {:b}". format(x, y))
  print(a, b)
  sleep(1)


  


#for i in range(8):           # 8 bits in register
#  GPIO.output(self.dataPin, ~(byteVal & (1<<i)))  # if common anode
