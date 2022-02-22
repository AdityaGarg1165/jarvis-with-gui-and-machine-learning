import json
from ntpath import join
import  pyjokes
import  pyautogui
import wikipedia
import random
import sys
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


class Main(QThread):
    def __init__(self):
        super(Main,self).__init__()

    def run(self):
        while True:
            # self.query = self.TakeCommand()
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
            
                
            if 'open stackoverflow' in self.query:
                webbrowser.open("www.stackoverflow.com")

            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")


            elif 'a joke' in self.query:
                say(pyjokes.get_joke())

            elif 'guess game' in self.query:
                randnum = random.randint(0,50)
                say("guess the number")
                user_said = self.TakeCommand()
                try:
                    if int(user_said) == randnum:
                        say("you guessed the number correct")
                    else:
                        say("you failed to guessed the number")
                except:
                    say("please say a number")


            
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
        


            elif 'open' in self.query:
                try:
                    user_query = self.query
                    user_query = user_query.split(" ")
                    if 'firefox' == user_query[1]:
                        os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
                    
                    if 'vscode' in self.query:
                        os.startfile("C:\\Users\\pc\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe")

                    if 'notepad' in self.query:
                        os.system("notepad")
                    if 'skype' in self.query:
                        os.system("skype")
                    
                    if 'chrome' == user_query[1]:
                        os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
                    else:
                        webbrowser.open(user_said[1])

                except:
                    say("sir please specify an program")
                

            
            elif 'search google' in self.query:
                self.sq = self.TakeCommand().lower()
                webbrowser.open(f"{self.sq}")

            elif 'wikipedia' in self.query:
                user_query = self.query
                user_query = user_query.replace("wikipedia",'')
                user_query = user_query.replace("search",'')
                summary = wikipedia.summary(user_query,sentences=2)
                say("according to wikipedia")
                say(summary)

            elif 'how to do mode' in self.query:
                self.search = self.TakeCommand().lower()
                say("what should i search")
                how_to = pywikihow.search_wikihow(self.search,max_results=1)
                say(how_to[0].summary)

            elif 'quit' in self.query:
                app.quit()

            elif 'what is the time' in self.query:
                say("sir the time is")
                say(f"{datetime.datetime.now().hour - 12}")
                say(f"{datetime.datetime.now().minute}")


            elif 'the date' in self.query:
                say(datetime.datetime.now().date)

            elif 'the day' in self.query:
                say(f"the date is{datetime.datetime.now().day}")

            elif 'what is' in self.query:
                quer = self.query
                try:
                    b = []
                    quer = quer.split("is")
                    quer.pop(0)
                    for i in range(len(quer)):
                        quer = quer[0].split("+")
                    for iterator in range(len(quer)):
                        b.append(int(quer[iterator]))
                    for iter in range(len(quer)):
                        result = sum(b)
                    say(result)

                except:
                    quer = quer.split(" ")          
                    user_said = self.query
                    user_said = user_said.split(" ")
                    result = wikipedia.summary(user_said[2])
                    say("according to wikipedia")
                    say(result)

            elif 'who is' in self.query:
                try:
                    user_query = self.query
                    user_query = user_query.split(" ")
                    if len(user_query) == 3:
                        summary = wikipedia.summary(user_query[2],sentences=2)
                        say("according to wikipedia")
                        say(summary)
                    elif len(user_query) == 4:
                        summary = wikipedia.summary(user_query[2] + user_query[3],sentences=2)
                        say("according to wikipedia")
                        say(summary)
                except:
                    pass

            elif 'wikipedia' in self.query:
                search = self.query.replace("wikipedia","")
                say(wikipedia.summary(search))

            elif 'iphone price' in self.query:
                html = requests.get("https://www.flipkart.com/apple-iphone-13-midnight-128-gb/p/itmca361aab1c5b0?pid=MOBG6VF5Q82T3XRS&lid=LSTMOBG6VF5Q82T3XRSOXJLM9&marketplace=FLIPKART&q=iphone+13&store=tyy%2F4io&srno=s_1_2&otracker=search&otracker1=search&fm=Search&iid=b3c3f505-c7bb-4709-bda9-7fb5a1546c56.MOBG6VF5Q82T3XRS.SEARCH&ppt=sp&ppn=sp&ssid=x3drt85jc7dm8zk01645241851373&qH=c68a3b83214bb235")
                htmldata = html.content
                tomato_soup = bs4.BeautifulSoup(htmldata,'html.parser')
                print(tomato_soup.find('div',class_="_30jeq3 _16Jk6d").get_text())
                say(tomato_soup.find('div',class_="_30jeq3 _16Jk6d").get_text())
            
            elif 'who am i' in self.query:
                if not name == None:
                    say(f"Your name is {name}")
                else:
                    say("Sorry but i didnt recognize you")
            

            elif 'remember my name' in self.query:
                say("sir please tell your name")
                user_query = self.TakeCommand()
                with open(os.path.join(BASE_DIR,"files/name.txt")) as f:
                    f.write(user_said)
                    say("ok i will remember your name")

            
            
            elif 'set alarm' in self.query:
                import modules.alarm

            elif 'rock paper' in self.query:
                randnum = random.randint(1,3)
                if randnum == 1:
                    say("scissors")
                if randnum == 2:
                    say("paper")
                if randnum == 3:
                    say("rock")
                
            elif "None" in self.query:
                say("")
            
            else:
                results = model.predict([bag_of_words(self.query, words)])
                results_index = numpy.argmax(results)
                tag = labels[results_index]
                for tg in data["intents"]:
                    if tg['tag'] == tag:
                        responses = tg['responses']
                        say(random.choice(responses))

                


main_thread = Main()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Gui()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.stop)

    def changeoutput(self,text):
        self.ui.out.setText(text)
    def start(self):
        self.ui.movie = QMovie(os.path.join(BASE_DIR,"files\\gui.gif"))
        self.ui.movie2 = QMovie(os.path.join(BASE_DIR,"files\\earth.gif"))
        self.ui.label.setMovie(self.ui.movie)
        self.ui.earthgif.setMovie(self.ui.movie2)
        self.ui.movie.start()
        self.ui.movie2.start()
        main_thread.start()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.time)
        self.timer.start(1000)

    def time(self):
        self.hour = datetime.datetime.now().hour
        self.minute = datetime.datetime.now().minute
        self.second = datetime.datetime.now().second
        self.ui.label_2.setText(f"{self.hour}:{self.minute}:{self.second}")

    def stop(self):
        app.quit()

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    jarvis = MainWindow()
    jarvis.show()
    jarvis.start()
    sys.exit(app.exec_())
    