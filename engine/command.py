import pyttsx3
import speech_recognition as sr
import eel
import random as rd
import time

def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning...")
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source,10,5)

        try:
            print("understandig...")
            eel.DisplayMessage('understandig...')
            query = r.recognize_google(audio, language='am-en')
            print(f"you said: {query}\n")
            eel.DisplayMessage(query)
            time.sleep(2)
            
        except Exception as e:
            return ""
        
        return query.lower()
        
@eel.expose
def allCommands():   
     
    try:
        query = takecommand()
        print(query)
    
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube" or "በዩቲዩብ":
            from engine.features import PlayYoutube
            PlayYoutube(query)
            
        else:
            print("not run")    
    except:
        print("error")    
        
    eel.ShowHood()        


        




 
        
               
        
        
        
       