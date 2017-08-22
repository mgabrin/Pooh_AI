from pooh_models import db, PoohUser
import json

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
				print('I\'ll remember that')
				return ('I\'ll remember that')
			else:
				print('No user')
	return builder

def profileAccessor(app, command):
	def accessor():
		with app.app_context():
			user = PoohUser.query.filter_by(name = curUser).first()

			if user:
				if 'my name' in command:
					print(f'Your name is {user.name}')
					return (f'Your name is {user.name}')
				else:
					userInfo = json.loads(user.additional_info)
					for key, val in userInfo.items():
						if key in command:
							print(f'Your {key} is {val}')
							return(f'Your {key} is {val}')
					print('I don\'t know that yet. Please teach me.')
					return('I don\'t know that yet. Please teach me.')

			else:
				print('No user')
				return('No user')
	return accessor

def switchUser(app, userName):
	def switch():
		with app.app_context():
			lookupUser = PoohUser.query.filter_by(name = userName).first()

		if lookupUser:
			print(f'Hello, {userName}')
			return(f'Hello, {userName}')
			curUser = userName
		else:
			print(f'Welcome, {userName}')
			return(f'Welcome, {userName}')
			newUser = PoohUser(userName)
			with app.app_context():
				curUser = userName
				db.session.add(newUser)
				db.session.commit()

			
	return switch