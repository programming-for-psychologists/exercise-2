# Now let's implement some feedback. Let's allow either a 'f' or 'l' response for each trial. 
#If the response is correct, show a green 'O' before the start of the next trial. If the response is wrong, 
#show a red 'X' (you can use textStim objects for feedback). Show the feedback for 500 ms. 

import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
firstNames= [name.split(' ')[0].rstrip() for name in names]
lastNames = [name.split(' ')[1].rstrip() for name in names]
allNames = firstNames + lastNames

win = visual.Window([800,600],color="black", units='pix')
fixation =  		visual.TextStim(win,text="+", height=40, color="white",pos=[0,0])
correctFeedback = 	visual.TextStim(win,text="O", height=50, color="green",pos=[0,0])
incorrectFeedback =	visual.TextStim(win,text="X", height=50, color="red",pos=[0,0])

nameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])

while True:
	nameShown = random.choice(allNames)
	nameStim.setText(nameShown)

	fixation.draw()
	win.flip()
	core.wait(.5)
	win.flip()

	nameStim.draw()
	win.flip()

	responseReceived= event.waitKeys(keyList= ['f','l'])[0]

	if (nameShown in firstNames and responseReceived=='f') or (nameShown in lastNames and responseReceived=='l'):
		correctFeedback.draw()
	else:
		incorrectFeedback.draw()
	win.flip()
	core.wait(.5)
	win.flip()

	if event.getKeys(['q']):
		break

