#Create a fixation cross using a TextStim object visual.TextStim set text to "+" and color to "white". 
#Make the fixation cross appear for 500 ms before each name and disappears right before the name comes up.

import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]


win = visual.Window([800,600],color="black", units='pix')
fixation= visual.TextStim(win,text="+", height=40, color="white",pos=[0,0])
firstNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])

while True:
	nameShown = random.choice(firstNames)
	firstNameStim.setText(nameShown)

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