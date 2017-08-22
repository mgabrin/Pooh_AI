import threading
import os
import logging
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask_restful import reqparse, abort, Api, Resource
from pooh_delegator import delegator, startThread
from pooh_models import db, PoohUser

import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
app.config.update(dict(
	DEBUG=True,
	SECRET_KEY='development key',
	USERNAME='admin',
	PASSWORD='default',
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app.root_path, 'pooh.db'),
	SQLALCHEMY_TRACK_MODIFICATIONS = False,
	SEND_FILE_MAX_AGE_DEFAULT = 1
))
db.init_app(app)
api = Api(app)
curUser = 'mike'

@app.route('/')
def root():
	return render_template('index.html');

def start():
	print('Hello, Mike')
	while True:
		task = input("> ")
		thread = startThread(delegator(app, task))
		thread.join()

def startApp():
	app.run(host='127.0.0.1', port=3000, debug=False)

class General(Resource):
	def post(self):
		response = delegator(app, request.data.decode("utf-8"))()
		return response

api.add_resource(General, '/general')

if __name__ == '__main__':
	stThread = startThread(start)
	startThread(startApp)
	stThread.join()

