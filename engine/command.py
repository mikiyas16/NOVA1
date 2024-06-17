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
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()

for i in range(3):
    
    print("this particular device is password protected, please enter the require password")
    a = input("Enter Password to open NOVA :- ")
    pw_file = open("D:\\miki file\\atom codes\\jarvis miki\\nova\\password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! ")
        break
    elif (i==2 and a!=pw):
        exit()
        
    elif (a!=pw):
        print("incorrect password")

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
    
    query = takecommand()
    print(query)
    
    if "open" in query:
        from engine.features import openCommand
        openCommand(query)
    elif "on youtube":
        from engine.features import PlayYoutube
        PlayYoutube(query)
            
    else:
        print("not run")    
        
    eel.ShowHood()        


        




 
        
               
        
        
        
       