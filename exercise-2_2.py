# Open names.txt to see what the names list looks like. 
# Make the script show last names instead of first names (don't change the names.txt file).
import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
lastNames = [name.split(' ')[1] for name in names]


win = visual.Window([800,600],color="black", units='pix')
fixation= visual.TextStim(win,text="+", height=40, color="white",pos=[0,0])
firstNameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])

while True:
	nameShown = random.choice(lastNames)
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