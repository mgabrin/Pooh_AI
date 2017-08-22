import datetime
import time

timerStart = time.time()
timerEnd = time.time()

def timeStart(command):
	def time():
		if 'timer' in command:
			return getTimer(command)
		else:
			return getCurTime()
	return time
			

def getCurTime():
	print('\nThe current time is', datetime.datetime.now(), '\n')
	return (f'The current time is {str(datetime.datetime.now())}')

def getTimer(command):
	if 'start' in command:
		timerStart = time.time()
		return ('Started')
	elif 'stop' in command:
		timerEnd = time.time()	
		print(f'Elapsed time: {timerEnd - timerStart}')
		return (f'Elapsed time: {timerEnd - timerStart}')
		timerStart = 0
		timerEnd = 0