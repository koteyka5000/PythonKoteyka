from tkinter import *
from random import choice
from time import time

root = Tk()
root.geometry('300x200')
root['bg'] = 'cyan'
root.title('game')

def generateRandomKey():
    keys = ('z', 'x', 'c')
    key = choice(keys)
    return key if key != keyNow else generateRandomKey()

run = True
keyNow = 'z'
keyNow = generateRandomKey()

keyLabel = Label(root, text=keyNow, font='Arial, 35', bg='cyan')
keyLabel.place(x=130, y=60)

timeLabel = Label(root, text='', bg='cyan', font='Arial, 20')
timeLabel.place(x=110, y=120)

timeNow = time()
timeList = []

def pressed(key):
    global keyNow, keyLabel, run, timeNow, timeList
    if run:
        if key == keyNow:
            keyNow = generateRandomKey()
            keyLabel.configure(text=keyNow)

            timeList.append(round(time() - timeNow, 2))
            timeNow = time()
            timeToShow = round(sum(timeList) / len(timeList), 2)
            timeLabel.configure(text=timeToShow)
        else:
            run = False
            keyLabel.configure(text='')
            Label(root, text=f'Проигрыш!\nБыла нажата -{key}-, а нужно было -{keyNow}-',\
                bg='cyan', font='Arial 14').place(x=0, y=60)

root.bind('z', lambda event: pressed(key='z'))
root.bind('x', lambda event: pressed(key='x'))
root.bind('c', lambda event: pressed(key='c'))
root.mainloop()