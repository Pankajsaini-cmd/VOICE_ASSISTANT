import pyttsx3
from os.path import isfile, join
import fnmatch,os
import scrappyweb
from os import listdir
import requests
import json
from word2number import w2n
# import pyaudio
import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
import time
import random
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr
from datetime import date
now = date.today()
print(sr.__version__)
now1=now.strftime("%d/%m/%Y")
# engine = pyttsx3.init('sapi5')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

# //////////////This is for testing purpose 

# def find_files(filename, search_path):
#    result = []
#    for root, dir, files in os.walk(search_path):
#       if filename in files:
#          result.append(os.path.join(root, filename))
#    return result

# /////////////////////////////////////////////
def hit(key):
    pyautogui.keyDown(key)
    return
def isCollide(data):
    # Draw the rectangle for birds
    for i in range(340, 450):
        for j in range(410, 563):
            if data[i, j] < 100:
                hit("down")
                return
    for i in range(500, 580):
        for j in range(563, 700):
            if data[i, j] < 100:
                hit("up")
                return
    return


def speak(audio):
    engine.setProperty('rate', 170)
    engine.say(audio)
    engine.runAndWait()
# def search(list, platform):
#     for i in range(len(list)):
#         if list[i] == platform:
#             return True
#     return False
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Pankaj Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Pankaj Sir")
    else:
        speak("Good evening Pankaj Sir")
    speak("how may i help you sir")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # speak("I am listening sir")
        r.pause_threshold = 1
        r.energy_threshold = 500
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print(audio)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.
    except Exception as e:
        print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
def func1(url):
    r=requests.get(url)
    r1=r.text
    user=json.loads(r1)
    r2=user['articles']
    speak("today's latest news is")
    for i in r2:
        print(i['title'])
        speak(i['title'])
        print(i['description'])
        speak(i['description'])
        print("\n")
        speak("Next News")
        time.sleep(1.5)
    speak("News finished   Bye and have a nice day")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        lenght = len(query)
        print(lenght)
        if lenght>5:
            if 'wikipedia' in query:
                speak("searching wikipedia Pankaj Sir")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                speak(results)
            elif 'how are you' in query:
                speak("I am good sir, i hope you're also good")
            elif 'on youtube' in query:
                query = query.replace("youtube", "")
                query = query.replace("search", "")
                query = query.replace("on", "")
                webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
            elif 'on google' in query:
                query=query.replace("on google","")
                query=query.replace("search","")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            elif 'on stackoverflow' in query:
                query=query.replace("search","")
                query=query.replace("on stackoverflow","")
                query=query.replace(" ",'+')
                webbrowser.open(f"https://stackoverflow.com/search?q={query}")
            elif 'play music' in query:
                num = len(fnmatch.filter(os.listdir('D:\\PANKAJ SAINI\\Songs'),'*.mp3'))
                tata = random.randint(0,num)
                music_dir = 'D:\\PANKAJ SAINI\\Songs'
                songs = fnmatch.filter(os.listdir(music_dir),'*.mp3')
                os.startfile(os.path.join(music_dir,songs[tata]))
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir,the time is {strTime}")
            elif 'date' in query:
                print(now1)
                speak(f"Sir,The date is {now}")
            elif 'open code' in query:
                codePath = 'C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
                os.startfile(codePath)
            elif 'dino game' in query:
                speak("let's play dino game sir, i'll try my best to play")
                os.system(f'start chrome')
                time.sleep(2)
                speak("sir.. i'll start play in 8 seconds please enter chrome://dino")
                time.sleep(8)
                # hit('up') 
                while True:
                    image = ImageGrab.grab().convert('L')  
                    data = image.load()
                    # print(data)
                    isCollide(data)
            # elif 'open application' or 'open app' in query:
            #     speak("Sir, Which app do you like to open")
            #     query = takeCommand().lower()
            #     query = query.replace("jarvis", "")
            #     speak(f"sir, i am going to open {query}")
            #     os.system(f'start {query}')
            #     for1 = os.listdir('D:\\PANKAJ SAINI')
            #     if search(for1, query):
            #         os.startfile(query)
            #     else:
            #         speak("Sir, i didn't find any application")
            # elif 'find' or 'search' in query:
            #     query = query.replace("find search","" )
               
            elif 'shut up' in query:
                speak('bye pankaj sir i am shutting up')
                exit()
            elif 'shutdown system' in query:
                speak("are you sure sir, for shutdown")
                query2 = takeCommand().lower()
                if 'sure' in query2:
                    os.system("shutdown /s /t 30")
                    speak("have a nice time sir,I am shutting down system in 30 seconds")
                    query3 = takeCommand().lower()
                    if 'just kidding' in query3:
                        os.system("shutdown /a")
                        speak("nice joke sir, you are just going to kill me sir")
                    else:
                        continue
                else:
                    continue
            elif 'extract data from amazon' in query:
                speak("which data you want to extract, that Laptop,mobile Etcetera")
                query1 = takeCommand().lower()
                print(query1)
                if query1:
                    speak("How many pages you want to extact")
                    query2 = takeCommand().lower()
                    try:
                        query2 = w2n.word_to_num(query2)
                    except:
                        speak("sorry sir! unable to understand")
                        continue
                    speak("relax sir now i will extract data")
                    try:
                        scrappyweb.main(query1,query2)
                        speak("I done my work of data scrapping")
                    except:
                        speak("I found some error that is like")
                else:
                    continue
            elif 'hear news' in query:
                speak("sir i have three country's news, its India, China, united states and mix news, which would you preffer")
                query = takeCommand().lower()
                try:
                    if 'india' in query:
                        url = ('http://newsapi.org/v2/top-headlines?''country=in&''apiKey=HERE YOUR API KEY OF NEWSAPI')
                        speak("Top headlines from India")
                        func1(url)
                    elif 'china' in query:
                        url = ('http://newsapi.org/v2/top-headlines?''country=cn&''apiKey=HERE YOUR API KEY OF NEWSAPI')
                        speak("Top headlines from China")
                        func1(url)
                    elif 'united states' in query:
                        url = ('http://newsapi.org/v2/top-headlines?''country=us&''apiKey=HERE YOUR API KEY OF NEWSAPI')
                        speak("Top headlines from United States")
                        func1(url)
                    elif 'mix' in query:
                        url = ('http://newsapi.org/v2/top-headlines?'
                        'sources=bbc-news&'
                        'apiKey=040044a0148442458ad670d1aa3981ba')
                        speak("Top headlines from BBC news")
                        func1(url)
                except Exception as e:
                    print(e)
                    speak('sorry could not understand sir')
            else:
                speak("Sir i have no instruction for this command, may be i'll do it later after new update, you can try another command")
