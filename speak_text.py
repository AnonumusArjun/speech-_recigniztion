import speech_recognition as sr
import webbrowser as wb

r = sr.Recognizer()

with sr.Microphone() as source:
	print('Speak anything ')
	audio = r.listen(source)
	try:

		text = r.recognize_google(audio)
		print('You said : {}'.formate(text))
	except: 
		print("Coud not Recognize voice")