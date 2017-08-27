from pooh_models import db, PoohUser
import json
from pooh_io import output

curUser = 'mike'

def profileBuilder(app, command):
	def builder():
		with app.app_context():
			user = PoohUser.query.filter_by(name = curUser).first()

			if user:
				key = " ".join(command.split()[1:command.split().index("is")])
				val = " ".join(command.split()[command.split().index("is")+1:])


				userInfo = json.loads(user.additional_info)
				userInfo[key] = val
				user.additional_info = json.dumps(userInfo)
				db.session.commit()
				output('I\'ll remember that')
				return ('I\'ll remember that')
			else:
				output('No user')
	return builder

def profileAccessor(app, command):
	global curUser
	def accessor():
		global curUser
		with app.app_context():
			user = PoohUser.query.filter_by(name = curUser).first()
		if user:
			if 'my name' in command:
				output(f'Your name is {curUser}')
				return (f'Your name is {curUser}')
			else:
				userInfo = json.loads(user.additional_info)
				for key, val in userInfo.items():
					if key in command:
						output(f'Your {key} is {val}')
						return(f'Your {key} is {val}')
				output('I don\'t know that yet. Please teach me.')
				return('I don\'t know that yet. Please teach me.')

		else:
			output('No user')
			return('No user')
	return accessor

def switchUser(app, userName):
	global curUser
	def switch():
		global curUser
		with app.app_context():
			lookupUser = PoohUser.query.filter_by(name = userName).first()

		if lookupUser:
			output(f'Hello, {userName}')
			curUser = userName
			return(f'Hello, {userName}')
		else:
			output(f'Welcome, {userName}')
			newUser = PoohUser(userName)
			curUser = userName
			with app.app_context():
				
				db.session.add(newUser)
				db.session.commit()
			return(f'Welcome, {userName}')

	return switch