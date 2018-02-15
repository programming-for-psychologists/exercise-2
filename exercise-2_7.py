#Pop up a box that accepts a first name, and check to make sure that the name exists. 
#If it doesn't, pop-up a 'Name does not exist'error box


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
userVar = {'Name':'Enter a first name'}

def popupError(text):
    errorDlg = gui.Dlg(title="Error", pos=(200,400))
    errorDlg.addText('Error: '+text, color='Red')
    errorDlg.show()


while True:
	dlg = gui.DlgFromDict(userVar)
	if userVar['Name'] not in firstNames:
		popupError('Not a valid first name')
	else:
		break

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

