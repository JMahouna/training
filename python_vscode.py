import random

print('your password')

char='12&é34ùmp^$*!:ml:;!/.?/§ùmp^µ£_-wxc>><<dà)=+1234MAPEN?SNFUTIOOOCNJSK'

password=''

for x in range(16) :
    password+=random.choice(char)

print(password)