from pooh_talk import poohTalk
import copy

queueMessage = ''

def output(message):
	global queueMessage
	print(message)
	poohTalk(message)
	queueMessage = message

def checkMessage():
	global queueMessage
	temp = copy.deepcopy(queueMessage)
	queueMessage = ''
	return temp
