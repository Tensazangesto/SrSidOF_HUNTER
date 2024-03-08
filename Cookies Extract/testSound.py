from gtts import gTTS
from os import system

sound = gTTS(text="helloo world", lang="en")
sound.save("sound.mp3")
system("start sound.mp3")