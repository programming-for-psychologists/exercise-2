# On each presentation of a name, wait for a response ('f' for first name, 'l' for last-name) 
#and only proceed to the next name if the response is correct. Hint: if you've done steps 2-3 properly, 
#this should be really easy. Refer to the psychopy documentation of event.waitKeys() if you have trouble.

import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
firstNames= [name.split(' ')[0].rstrip() for name in names]
lastNames = [name.split(' ')[1].rstrip() for name in names]
allNames = firstNames + lastNames
print lastNames


win = visual.Window([800,600],color="black", units='pix')
fixation= visual.TextStim(win,text="+", height=40, color="white",pos=[0,0])

nameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])

while True:
	nameShown = random.choice(allNames)
	nameStim.setText(nameShown)


	if nameShown in firstNames:
		correctResponse='f'
	elif nameShown in lastNames:
		correctResponse='l'
	else:
		print 'uh oh'

	fixation.draw()
	win.flip()
	core.wait(.5)
	win.flip()

	nameStim.draw()
	win.flip()

	event.waitKeys(keyList= [correctResponse])


	if event.getKeys(['q']):
		break

