from win32com.client import Dispatch
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
def speak(audio):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(audio)    

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning raj")
    elif hour>=12 and hour<18:
        speak("Good Afternoon raj")
    else:
        speak("Good evening raj")
    speak("I am jarvis sir and you are my boss. so tell me how can I help you?")

def take_command():
    #it takes microphone input gfrem the user and returns string output..
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("LIstening....")
        r.pause_threshold = 1
        audio = r.listen(source)


        try:
            print("Recognising....")
            querry = r.recognize_google(audio, language='en-in')
            print(f"User said: {querry}\n")

        except Exception as e:
            print("Say that again please....")
            return "None"         
        return querry
if __name__ == "__main__":
    wishMe()    
    while(True):
        querry =  take_command().lower()

    #Logic for executing task based on querry

        if 'wikipedia' in querry:
            speak("Searching wikipedia")
            querry = querry.replace("wikipedia", "")
            results = wikipedia.summary(querry, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in querry:
            webbrowser.open("youtube.com")

        elif 'open google' in querry:
            webbrowser.open("google.com")
        elif 'open facebook' in querry:
            webbrowser.open("facebook.com")
        elif 'play music' in querry:
            music_dir = "E:\\New audio song"
            songs = os.listdir(music_dir)
            print(songs)
            i = random.randint(0, len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[i]))
        elif 'the time' in querry:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")
        elif 'open code' in querry:
            codepath = "C:\\Users\\rajsr\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  
            os.startfile(codepath)    
        if 'exit' in querry:
            break     