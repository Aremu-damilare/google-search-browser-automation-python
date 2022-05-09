#import library

import speech_recognition as sr
import time

# Initialize recognizer class (for recognizing the speech)
from main import browse
r = sr.Recognizer()
import pyttsx3

# Reading Microphone as source
# listening the speech and store in audio_text variable

# while True:
def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def getAudio():
    with sr.Microphone() as source:
        SpeakText("command me:")
        # print("Hi, command me")
        audio_text = r.listen(source)
        print("Time over. process....")
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        
        try:
            text = r.recognize_google(audio_text)
            # using google speech recognition
            SpeakText("you said")
            # print("You said: "+text)
            SpeakText(text)
            return text
            
        except:
            SpeakText("Sorry, I did not get that")
            return print("Sorry, I did not get that")

# time.sleep(5)

while True:
    browse(getAudio())
