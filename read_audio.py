import speech_recognition as sr

r = sr.Recognizer()

PATH = 'a.mp3'

with sr.AudioFile(PATH) as source:
	audio = r.record(source)

	print(r.recognize_sphinx(audio))