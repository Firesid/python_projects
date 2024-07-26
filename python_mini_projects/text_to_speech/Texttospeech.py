from gtts import gTTS #we have imported this module for text to speech conversion
import os

text = "Hello everyone. How are you guys doing?" #text that we want to convert
language = 'en' #en is for english language
obj = gTTS(text = text, lang= language, slow = False)
#we have used slow = False because our converted video will have a high speed
obj.save("sample.mp3")

#to open the file automatically we have to import OS
os.system("sample.mp3")
