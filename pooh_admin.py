from pooh_models import db, PoohUser
from subprocess import call
import os

def adminStart(app):
	def admin():
		username = input("Enter the admin username: ")
		password = input("Enter the admin password: ")

		if username == 'mike' and password == 'gretta':
			while True:
				task = input("ADMIN > ")
				if task == 'initialize db':
					with app.app_context():
						db.create_all()
						print('I will store all of my memories here.')
				elif task == 'drop db':
					call(['rm', 'pooh.db'], stdout=open(os.devnull, 'wb'))
					print('Ok, I have deleted my memory.')
				elif 'exit' in task:
					print('Exiting admin mode')
					return
		else:
			print('Invalid Credentials')
	return admin