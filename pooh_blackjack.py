from random import randint
from pooh_models import db, PoohBlackJack
import copy
from pooh_io import output

cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',
'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',
'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',
'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

def getCard(handCards):
	cardIndex = randint(0,len(handCards)-1)
	card = handCards[cardIndex]
	handCards.pop(cardIndex)
	return card

def toString(handCards):
	string = ''
	for card in handCards:
		string = string + card
	return string

def calculateOdds(hand, handCards):
	positive = 0
	for card in handCards:
		hand.append(card)
		possibleSum = sum(hand)
		hand.remove(card)

		if possibleSum <= 21:
			positive = positive + 1

	return (positive/len(handCards))



def sum(hand):
	total = 0
	for card in hand:
		if card == 'Ace':
			total = total + 1
		elif card == 'Jack':
			total = total + 10
		elif card == 'Queen':
			total = total + 10
		elif card == 'King':
			total = total + 10
		else:
			total = total + int(card)
	return total

def play(app):
	while True:
		handCards = copy.deepcopy(cards)

		# Dealing Pooh's cards
		poohHand = [getCard(handCards), getCard(handCards)]
		
		# Dealing the players cards
		playerHand = [getCard(handCards), getCard(handCards)]


		output(f'Pooh Hand: {poohHand[0]}, {poohHand[1]} ({sum(poohHand)})')
		output(f'Player Hand: {playerHand[0]}, {playerHand[1]} ({sum(playerHand)})')
		
		
		# Asking the user if they would like to hit
		decision = ''
		while decision.lower() != 'stay':
			decision = input("Hit or Stay? ")
			if decision.lower() == 'hit':
				playerHand.append(getCard(handCards))
				output(f'Player Hand: {playerHand} ({sum(playerHand)})')
				if sum(playerHand) > 21:
					output('You busted')
					decision = 'stay'
		
		# Deciding if Pooh should hit
		# Check to see if we have encountered this hand before
		if sum(playerHand <= 21):
			with app.app_context():
				decision = ''
				while decision.lower() != 'stay':
					playerHandString = toString(playerHand)
					poohHandString = toString(poohHand)
					previousData = PoohBlackJack.query.filter_by(playerHand = playerHandString).filter_by(poohHand = poohHandString).all()
					
					# If we have encountered this hand, ensuring we have seen it at least 10 times
					if len(previousData) > 10:
						# if we have, then we want to use the historical statistics to make our decision
						output('in here')
					# If we haven't, we want to play the probablilities of the cards remaining in the deck
					else:
						odds = calculateOdds(poohHand, handCards)
						if odds > .5:
							poohHand.append(getCard(handCards))
						else:
							output(f'Pooh Hand: {poohHand} ({sum(poohHand)})')
							decision = 'stay'

		game = PoohBlackJack(playerHandString, poohHandString)
		if sum(playerHand) > 21:
			output('Pooh wins')
		elif sum(poohHand) > 21:
			output('Player wins!')
		elif sum(poohHand) > sum(playerHand):
			output('Pooh wins!')
		elif sum(poohHand) < sum(playerHand):
			output('Player wins')
		else:
			output('Draw!')
		output('\n----------------------------------\n')

if __name__ == '__main__':
	play()