# Now, instead of waiting for a response forever, let's implement a timeout. 
# Show accuracy feedback as before, but now also show a red 'X' if no response is received for 1 sec 
# (and go on to the next trial automatically following the feedback).

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

	responseReceived= event.waitKeys(maxWait=1.0, keyList= ['f','l'])
	if responseReceived==None:
		responseReceived='NA'
	else:
		responseReceived=responseReceived[0]

	if (nameShown in firstNames and responseReceived=='f') or (nameShown in lastNames and responseReceived=='l'):
		correctFeedback.draw()
	else:
		incorrectFeedback.draw()

	win.flip()
	core.wait(.5)
	win.flip()

	if event.getKeys(['q']):
		break

