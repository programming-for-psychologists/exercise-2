# Extend the task by requiring the subject to respond by pressing a spacebar (the key is called 'space'), 
# as quickly as possible anytime the name on the screen matches the name you entered into the box 
# (so if I enter 'Gary' I would have to press 'space' anytime the name 'Gary' shows up. 
# If the participant presses 'space' to the wrong name (false alarm), or misses the name (a miss), show a red X.

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
userVar = {'Name':'Enter a first or last name'}

output_file = open("output.txt","w")

def popupError(text):
    errorDlg = gui.Dlg(title="Error", pos=(200,400))
    errorDlg.addText('Error: '+text, color='Red')
    errorDlg.show()

def sanitize_response(response):
    if response==None:
    	return response
    else:
    	return response[0]

while True:
	dlg = gui.DlgFromDict(userVar)
	if userVar['Name'] not in allNames:
		popupError('Not a valid first or last name')
	else:
		break

while True:
	nameShown = random.choice(allNames)
	nameStim.setText(nameShown)

	win.flip()
	core.wait(.25)

	fixation.draw()
	win.flip()
	core.wait(.5)
	win.flip()

	nameStim.draw()
	win.flip()
	responseTimer = core.Clock()

	if userVar['Name']==nameShown:
		correctResponse = 'space'
	else:
		correctResponse = None

	responseReceived= sanitize_response(event.waitKeys(maxWait=1.0, keyList=['space']))
	if responseReceived != None:
		RT = responseTimer.getTime()*1000
	else:
		RT = 'NA'

	if responseReceived==correctResponse:
		isRight=1
		correctFeedback.draw()
	else:
		isRight=0
		incorrectFeedback.draw()

	win.flip()
	core.wait(.5)
	win.flip()

	dataString = '\t'.join((str(isRight),str(RT)))
	output_file.write(dataString+'\n')
	output_file.flush() #flushes the file buffer to the file. Without this, data to the file is only written once the file is closed.

output_file.close()