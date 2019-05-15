import random

while True:
   number = random.randrange(1, 6)
   print(number)
   user = input('Do you Want to dice again')
   if user=='n' or user=='N':
       print(number)
       break;