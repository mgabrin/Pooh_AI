
def todoistStart(task):
	def todoist():
		if 'add' in task:
			addTask()
		elif 'what' in task:
			grabTask()
		elif 'mark' in task or 'finish' in task or 'complete' in task:
			completeTask()
		else:
			print('I\'m sorry, I couldn\'t complete that request.')
	return todoist


def addTask():
	print('adding')

def grabTask():
	print('grabbing')

def completeTask():
	print('completing')