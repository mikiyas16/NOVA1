import pyttsx3
import speech_recognition as sr
import sys
import datetime
import os

import subprocess
import webbrowser

from playsound import playsound

import random as rd

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


speakinghello = ["Hello! sir, How can I assist you today","Hey sir What can ido for you","Hi there!, How can I help you today","Hi sir!, How can I help you"]
speakinggoodbye = ['okay sir, you can call me anytime','ok sir, I am always here whenever you need assistance.','If you need assistance later, you can call me anytime']
speakingexeption = ["saythat again","I'm sorry sir, I didn't understand your request","please retalk it again",""]