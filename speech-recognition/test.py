import speech_recognition as sr
from os import path

# Add your key here
BING_KEY = ""

# Audio file <= 10 seconds long
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "voice.wav")

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)

try:
    print("Transcript " + r.recognize_bing(audio, key=BING_KEY))
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
