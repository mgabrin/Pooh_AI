import requests
from requests.auth import HTTPBasicAuth
import json
from subprocess import call
import os
import string
from pooh_io import output

def spotifyStart(task):
	def spotify():
		#if 'song' in task:
		if 'play' in task:
			requestType = 'track'
			path = 'tracks.items.[0].uri'
			wordArray = task.split()
			wordArray = wordArray[1:]

			# Doing some situational configuration
			if 'playlist' in task:
				requestType = 'playlist'
				wordArray.remove('playlist')
			elif 'album' in task or 'music by' in task:
				requestType = 'album'
				if 'album' in task:
					wordArray.remove('album')
				else:
					wordArray.remove('music')
					wordArray.remove('by')

				path = 'albums.items.[0]'
			elif 'artist' in task:
				requestType = 'artist'
				wordArray.remove('artist')
			
			songTitle = " ".join(wordArray)
			
			# Making the request for the resource we need
			token = spotifyAuth()['access_token']
			headers = {
				'Authorization': f'Bearer {token}'
			}
			query = {
				'q': songTitle,
				'type': requestType
			}
			r = requests.get('https://api.spotify.com/v1/search', headers = headers, params=query)
			call(['spotify', 'play', 'uri', json.loads(r.content)[f'{requestType}s']['items'][0]['uri']], stdout=open(os.devnull, 'wb'))
			
			output('Ok, here you go.')
		elif 'pause' in task or 'stop' in task:
			call(['spotify', 'pause'], stdout=open(os.devnull, 'wb'))
			output('Ok, stopped')
		elif 'next' in task:
			call(['spotify', 'next'], stdout=open(os.devnull, 'wb'))
			output('Can Do')
		elif 'prev' in task:
			call(['spotify', 'prev'], stdout=open(os.devnull, 'wb'))
			output('Whatever you say')
	return spotify


def spotifyAuth():
	data = {
		'grant_type':'client_credentials'
	}
	headers = {
		'Authorization': 'Basic MTYxZjU4Yjk2Y2M4NGRkYjlkYjk0YzM2MzEwOTdlMGE6YjYyNDU5MmJlYTUxNDNlY2IyM2RiZjY1OGExMWExYWE='
	}
	r = requests.post('https://accounts.spotify.com/api/token', data = data, auth=HTTPBasicAuth('161f58b96cc84ddb9db94c3631097e0a','b624592bea5143ecb23dbf658a11a1aa'))
	return json.loads(r.content)

