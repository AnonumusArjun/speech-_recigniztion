import speech_recognition as sr
import webbrowser as wb

r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
	print('[search Arjun: search Youtube]')
	print('Speak Now ...')
	audio = r3.listen(source)

if 'edureka' in r2.recognize_google(audio):
	r2 = sr.Recognizer()
	url = 'https://www.edureka.co/'
	with sr.Microphone() as source:
		print('Search your query ')
		audio = r2.listen(source)

		try:
			get = r2.recognize_google(audio)
			print(get)
			wb.get().open_new(url+get)
		except sr.UnknownValueError:
			print('Error')
		except sr.RequestError as e:
			print('Failed'.format(e)) 


if 'video' in r1.recognize_google(audio):
	r2 = sr.Recognizer()
	url = 'https://www.youtube.com/results?search_query='
	with sr.Microphone() as source:
		print('Search your query ')
		audio = r2.listen(source)

		try:
			get = r2.recognize_google(audio)
			print(get)
			wb.get().open_new(url+get)
		except sr.UnknownValueError:
			print('Error')
		except sr.RequestError as e:
			print('Failed'.format(e)) 
