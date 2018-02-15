#Make the program randomly alternate between first names and last names.

import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
firstNames= [name.split(' ')[0] for name in names]
lastNames = [name.split(' ')[1] for name in names]
allNames = firstNames + lastNames


win = visual.Window([800,600],color="black", units='pix')
fixation= visual.TextStim(win,text="+", height=40, color="white",pos=[0,0])

nameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])

while True:
	nameShown = random.choice(allNames)
	nameStim.setText(nameShown)

	fixation.draw()
	win.flip()
	core.wait(.5)
	win.flip()

	firstNameStim.draw()
	win.flip()
	core.wait(.75)
	win.flip()
	core.wait(.15)

	if event.getKeys(['q']):
		break