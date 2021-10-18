from collections import UserList
from io import open_code
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio) :
    engine.say(audio)
    engine.runAndWait()

def wishMe() :
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('GoodMorning Sir')
    elif hour>=12 and hour<16:
        speak('GoodAfterNoon Sir')
    
    elif hour>16 and hour<19:
        speak('GoodEvening Sir')

    else :
        speak('GoodNight Sir')




def takeComand() :

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 1000
        audio = r.listen(source)

    try:
        print('Recognising...')
        query = r.recognize_google(audio, language='eng-in')
        print(f'User said: {query}\n' )

    except Exception as e:
        # print(e)
        print('Say that again please...')
        return 'None'
    return query

def googleSearch() :
    command = input('Enter what to search : ')
    speak('Searcing Google')
    webbrowser.open(url='https://www.google.com/search?q=' + command)

def youtubeSearch() :
    command = input('Enter what to search : ')
    speak('Searcing youtube')
    webbrowser.open(url='https://www.youtube.com/results?search_query=' + command)
    

if __name__=="__main__" :
    while True:
        query =  takeComand().lower()

        if 'wikipedia' in query:
            speak('Searcing Wikipedia...')
            query = query.replace('wikipedia ', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According To Wikipedia')
            print(results)
            speak(results)

        elif 'how are you' in query:
            speak('I am good. Tell me what to do')

        elif 'wake up' in query:
            speak(wishMe())
            speak("I am Jarvis. Tell me what to do")

        elif 'sleep' in query:
            speak('Ok Sir! I am going to sleep')

        elif 'open dashboard' in query:
            speak('Opening whiteHat Junior dashboard')
            webbrowser.open_new(url='https://code.whitehatjr.com/s/dashboard')

        elif 'open projects' in query:
            speak('Opening whiteHat Junior projects')
            webbrowser.open_new(url='https://code.whitehatjr.com/s/my-projects')

        elif 'open snack' in query:
            speak('Opening snack')
            webbrowser.open_new(url='https://expo.dev/@amansamual?tab=snacks')

        elif 'open clock' in query:
            speak('Opening clock')
            webbrowser.open_new(url='https://aman16feb2007.github.io/Clock/')

        elif 'open amazon' in query:
            speak('Opening amazon')
            webbrowser.open_new(url= 'https://www.amazon.in/')

        elif 'google search' in query:
            googleSearch()

        elif 'youtube search' in query:
            youtubeSearch()

        elif 'open email' in query:
            speak('Opening email')
            webbrowser.open_new(url='https://mail.google.com/mail/u/0/#inbox')

        elif 'open marvel site' in query:
            speak('Opening marel site')
            webbrowser.open_new(url='https://www.marvel.com/')

        elif 'open epic games' in query:
            speak('Opening Epic Games')
            webbrowser.open_new(url='https://www.epicgames.com/store/en-US/')

        elif 'open wynk music' in query:
            speak('Opening wynk')
            webbrowser.open_new(url='https://wynk.in/music')

        elif 'song' in query:
            music_dir = 'C:\\BestSongs'
            songs = os.listdir(music_dir)
            speak('Playing Song')
            print(songs)
            os.startfile(os.path.join(music_dir, songs[random.randint(0, 31)]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            print(strTime)
            speak(f'Sir, The time is {strTime}')

        elif 'date' in query:
            strDate = datetime.date.today()
            print(strDate)
            speak(f'Sir, The Date is {strDate}')

        elif 'open visual studio code' in query:
            coPath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak('Opening visual studio code')
            os.startfile(coPath)

        elif 'open whatsapp' in query:
            whPath = "C:\\Users\\HP\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            speak('Opening whatsapp')
            os.startfile(whPath)

        elif 'open chrome' in query:
            chPath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            speak('Opening chrome')
            os.startfile(chPath)

        elif 'open teams' in query:
            tePath = 'C:\\Users\\HP\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart "Teams.exe"'
            speak('Opening Teams')
            os.startfile(tePath)