
def todoistStart(task):
	def todoist():
		if 'add' in task:
			addTask()
		elif 'what' in task:
			grabTask()
		elif 'mark' in task or 'finish' in task or 'complete' in task:
			completeTask()
		else:
			output('I\'m sorry, I couldn\'t complete that request.')
	return todoist


def addTask():
	output('adding')

def grabTask():
	output('grabbing')

def completeTask():
	output('completing')