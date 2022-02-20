import json
import  pyjokes
import  pyautogui
import wikipedia
import random
import sys
import PyQt5
import bs4
import pywikihow
import requests
import webbrowser
import cv2
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from modules.gui import Gui
from modules.nueralnetwork import *
from modules.spechrecognition import *
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


name = "Aditya"

model.load("model/model.pth")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)




def say(message):
    engine.say(message)
    engine.runAndWait()


class Main():
    def __init__(self):
        super(Main,self).__init__()

    def run(self):
        while True:
            self.query = input("a:").lower()
            if wake(self.query):
                self.TaskExecution()
            
    def whishMe(self):
        hour = int(datetime.datetime.now().hour)
        if hour <= 12:
            say(f"Good Morning {name} , I am Jarvis sir , how can i help you")

        elif hour >= 12 and hour < 20:
            say(f"Good Evening {name} , I am Jarvis sir , how can i help you")

        elif hour >= 12 and hour >= 20:
            say(f"Good Night {name} , I am Jarvis sir how can i help you")


    def TakeCommand(self):
        r = sr.Recognizer()

        with sr.Microphone() as source:
            r.pause_threeshold = 1
            audio = r.listen(source)
        try:
            self.query = r.recognize_google(audio,language="en-in")
            return self.query.lower()
        except:
            return "None"


    def TaskExecution(self):
        self.whishMe()
        while True:
            self.query = input("w:").lower()
            # self.query = self.TakeCommand()
            results = model.predict([bag_of_words(self.query, words)])
            results_index = numpy.argmax(results)
            tag = labels[results_index]
            for tg in data["intents"]:
                if tg['tag'] == tag:
                    responses = tg['responses']
                    
                    say(random.choice(responses))
                
            if 'open stackoverflow' in self.query:
                webbrowser.open("www.stackoverflow.com")

            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")
            
            elif sleep(self.query):
                self.query = "None"
                say("Okay,sir you can call me anytime")
                self.run()
            
            elif 'open camera' in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    _,frame = cap.read()


                    cv2.imshow('Frame',frame)
                    if cv2.waitKey(1) == 27:
                        break
                cv2.destroyAllWindows()
                cap.release()
            
            elif 'whatsapp' in self.query:
                pywhatkit.sendwhatmsg('+919958450057','hello',2,25)

            elif 'open cmd' in self.query:
                os.system("cmd")

            elif 'open notepad' == self.query:
                os.system("notepad")

            elif 'open vscode' in self.query:
                os.system("code")

            elif 'open firefox' in self.query:
                os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")

            

            elif 'search google' in self.query:
                self.sq = self.TakeCommand().lower()
                webbrowser.open(f"{self.sq}")

            elif 'how to do mode' in self.query:
                self.search = self.TakeCommand().lower()
                say("what should i search")
                how_to = pywikihow.search_wikihow(self.search,max_results=1)
                say(how_to[0].summary)

            elif 'what is' in self.query:
                quer = self.query
                quer = quer.split(" ")
                try:
                    op = quer[3]
                    if op == "plus":
                        num1 = int(quer[2])
                        num2 = int(quer[4])
                        say(num1 + num2)
                    elif op == "minus":
                        num1 = int(quer[2])
                        num2 = int(quer[4])
                        say(num1 - num2)
                    elif op == "divide":
                        num1 = int(quer[2])
                        num2 = int(quer[4])
                        say(num1 / num2)
                    elif op == "multiply":
                        num1 = int(quer[2])
                        num2 = int(quer[4])
                        say(num1 * num2)
                except:                    
                    user_said = self.query
                    user_said = user_said.split(" ")
                    result = wikipedia.summary(user_said[2])
                    say("according to wikipedia")
                    say(result)
            elif 'wikipedia' in self.query:
                search = self.query.replace("wikipedia","")
                say(wikipedia.summary(search))

            elif 'iphone price' in self.query:
                html = requests.get("https://www.flipkart.com/apple-iphone-13-midnight-128-gb/p/itmca361aab1c5b0?pid=MOBG6VF5Q82T3XRS&lid=LSTMOBG6VF5Q82T3XRSOXJLM9&marketplace=FLIPKART&q=iphone+13&store=tyy%2F4io&srno=s_1_2&otracker=search&otracker1=search&fm=Search&iid=b3c3f505-c7bb-4709-bda9-7fb5a1546c56.MOBG6VF5Q82T3XRS.SEARCH&ppt=sp&ppn=sp&ssid=x3drt85jc7dm8zk01645241851373&qH=c68a3b83214bb235")
                htmldata = html.content
                tomato_soup = bs4.BeautifulSoup(htmldata,'html.parser')
                print(tomato_soup.find('div',class_="_30jeq3 _16Jk6d").get_text())
                say(tomato_soup.find('div',class_="_30jeq3 _16Jk6d").get_text())
            
            elif 'set alarm' in self.query:
                import modules.alarm 
                
            elif "None" in self.query:
                say("")

def st():
    Main().TaskExecution()
st()