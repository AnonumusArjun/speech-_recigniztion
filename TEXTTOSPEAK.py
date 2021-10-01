from gtts import gTTS
import os

# Text input and it convert to give Voice
textt = input("Enter Text :")

language = 'en'

out = gTTS(text=textt, lang=language, slow=False)
out.save("voice.mp3")
os.system("voice.mp3")
