from pooh_time import timeStart
from pooh_spotify import spotifyStart
from pooh_todoist import todoistStart
from pooh_math import mathStart
from pooh_users import profileBuilder, switchUser, profileAccessor
from pooh_admin import adminStart
from pooh_blackjack import play
from pooh_models import db, PoohUser
from pooh_weather import getWeather
import threading
import os
from pooh_io import output

def delegator(app, task):
	# This is our exit point
	if 'quit' in task or 'goodbye' in task  or 'exit' in task:
		output('\nHave a good rest of your day, Michael\n')
		
		return
	# This will put us into admin mode if the user enters the correct username and password
	elif 'admin' in task.lower():
		return adminStart(app)
	# This is a basic property that will get us the time
	elif 'time' in task.lower():
		return timeStart(task)
	# This is where we will play something on spotify
	elif 'play' in task.lower() or 'pause' in task.lower() or 'stop' in task.lower() or 'next' in task.lower() or 'prev' in task.lower():
		return spotifyStart(task)
	# This is where we will be able to manipulate tasks in todoist
	elif 'todoist' in task.lower() or 'task' in task.lower() or 'to do' in task.lower():
		return todoistStart(task)
	# This is where we enter the blackjack game
	elif 'blackjack' in task.lower():
		return play(app)
	# This is where we go to get pooh to tell us the weather
	elif 'weather' in task.lower() or 'temperature' in task.lower():
		return getWeather(task)
	# This is where we can do basic mathematical operations. This will be expanded later
	elif '+' in task or '-' in task or '/' in task or '*' in task:
		return mathStart(task)
	# This is how we switch users so that Pooh will know what information to access about each user
	elif 'this is' in task.lower():
		curUser = "".join(task.split()[2:])
		return switchUser(app, curUser)
	elif '?' in task:
		return profileAccessor(app, task)
	elif 'my' in task.lower() and 'is' in task.lower():
		return profileBuilder(app, task)
	else:
		output('Sorry, I can\'t do that.')

def startThread(threadFunction):
	t = threading.Thread( target = threadFunction )
	t.setDaemon(1)
	t.start()
	return t