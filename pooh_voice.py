import speech_recognition as sr
from pooh_delegator import delegator, startThread
from pooh_io import output
def poohListen(app):
	def listen():
		while True:
			r = sr.Recognizer()
			with sr.Microphone() as source:
				audio = r.listen(source)
			try:
				speech = r.recognize_google(audio)
				print(f'> {speech}')
				thread = startThread(delegator(app, speech))

				thread.join()
			except:
				continue
	return listen


