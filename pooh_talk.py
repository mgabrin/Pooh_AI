from gtts import gTTS
import os
from subprocess import call

def poohTalk(speech):
	tts = gTTS(text=speech, lang='en-uk')
	tts.save("message.mp3")
	# this is for linux
	call(['mpg321', '-q', 'message.mp3'], stdout=open(os.devnull, 'wb'))