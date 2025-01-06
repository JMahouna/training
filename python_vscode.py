import random
from tkinter import *
from time import strftime

# ******* My code to generate my own message ***********

print('your password')

char='12&é34ùmp^$*!:ml:;!/.?/§ùmp^µ£_-wxc>><<dà)=+1234MAPEN?SNFUTIOOOCNJSK'

password=''

for x in range(16) :
    password+=random.choice(char)

print(password)

# ******** real-time clock GUI *********************

# myWindows = Tk() # initializing a windows
# myWindows.title('Real Time') 

# def time():
#     mytime = strftime('%H:%M:%S %p')
#     clock.config(text = mytime)
#     clock.after(1000, time)

# clock = Label(myWindows, font = ('arial',40,'bold'),
#               background= 'dark green',foreground = 'white')

# clock.pack(anchor = 'center')
# time()
# mainloop()

