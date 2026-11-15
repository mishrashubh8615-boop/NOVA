import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import os
from dotenv import load_dotenv

recognizer =  sr.Recognizer()
engine = pyttsx3.init()
load_dotenv()

newsapi = os.getenv("")

def processCommand(c):
    if 	'open google' in c.lower():
        webbrowser.open("http://google.com")

    elif 'open instagram' in c.lower():
        webbrowser.open("http://instagram.com")

    elif 'open youtube' in c.lower():
        webbrowser.open("http://youtube.com")

    elif 'news' in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = 	data.get('articles', [])

        for article in articles:
            speak(article['title'])
        

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    pass


def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing NOVA.....")

    while True:
        r = sr.Recognizer()
       


        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("listening.... ")
                audio = r.listen(source, timeout=5, phrase_time_limit=3 )
            word = r.recognize_google(audio)
            print("You said:", word)

            if "nova" in word.lower():
                print("NOVA ACTIVATED CONDITION DETECTED")
                speak("NOVA ACTIVATED")

                with sr.Microphone() as source:
                    print("NOVA active.... ")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5 )
                    command = r.recognize_google(audio)

                    processCommand(command)



                
        except Exception as e:
            print("Error; {0}".format(e))


 



