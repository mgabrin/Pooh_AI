from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PoohUser(db.Model):
	__tablename__ = 'person'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(40), nullable=False, unique=True)
	additional_info = db.Column(db.String(1000))

	def __init__(self, name):
		self.name = name
		self.additional_info = '{}'

	def __repr__(self):
		return (self.id)


class PoohBlackJack(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	playerHand = db.Column(db.String(40))
	poohHand = db.Column(db.String(40))
	hitWins = db.Column(db.Integer)
	hitLoses = db.Column(db.Integer)
	stayWins = db.Column(db.Integer)
	stayLoses = db.Column(db.Integer)

	def __init__(self, playerHand, poohHand):
		self.playerHand = playerHand
		self.poohHand = poohHand

	def __repr__(self):
		return (self.id)