import sys
import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import time
import pyautogui
import requests
import os
import wikipedia
import webbrowser
import speech_recognition as sr
import openai
import pyttsx3
from files.gui import Ui_MainWindow


openai.api_key = "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"
# text = ""
def t(t):
    global text
    text = t

def g():
    try:
        return text
    except:
        return ""


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


class Jarvis(QThread):
    def __init__(self):
        super(Jarvis,self).__init__()

    def run(self):
        self.Tasks()

    def Speak(self,text):
        engine.say(text)
        engine.runAndWait()

    def Listen(self):
        r = sr.Recognizer()

        with sr.Microphone() as mic:

            r.adjust_for_ambient_noise(mic,duration=0.2)
            r.pause_threshold = 0.5
            r.energy_threshold = 20

            self.audio = r.listen(mic)
        try:
            self.audio = r.recognize_google(self.audio,language="en-in")
            print(self.audio)
            return self.audio.lower()
        except:
            return "None"




    def GetReply(self,question,log = None):
        if(log == None):
            mf = open("log.txt","r")
            # mf = open("log.txt","r")
            log = mf.read()
            mf.close()
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f'{log}You:{question}\n mark :  ',
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        # chat_log=None,
        frequency_penalty=0,
        presence_penalty=0.6,
    )   
        answer = response["choices"][0]["text"]
        print("Mark:",str(answer).strip())
        self.Speak(answer.strip())
        # text = str(answer).strip()
        # t(str(answer.strip()))
        with open("log.txt","w") as f:
            f.write(log + f'\nYou:{question}\nMark:{answer}')


    def Tasks(self):
        self.Speak("Good Morning")
        while True:
            self.audio = self.Listen()
            # print(self.audio)
            # self.audio = input("You:")
            t(t=self.audio)

            if "open" in self.audio:
                split = self.audio.split(" ").__len__()
                spt = self.audio.split(" ")
                if split == 2:
                    if spt[1] == "spotify":
                        os.system("spotify")
                    if 'chrome' in self.audio:
                        webbrowser.open("http://")
                    if 'code' in self.audio:
                        os.system("code")
            elif "what all can you" in self.audio or "what can you" in self.audio:
                print("I can turn on your camera , play songs , open applications and many more")
                self.Speak("I can turn on your camera , play songs , open applications and many more")
            
            elif 'play music' in self.audio:
                os.system("spotify") 
                time.sleep(1)
                pyautogui.press("space")
                pyautogui.moveTo(1340,10) 
                pyautogui.click()

            # elif 'what is' in self.audio:
            #     rplc = self.audio.replace("what is","")
            #     try:
            #         spl = rplc.split("+")
            #         print(int(spl[0].strip()) + int(spl[1].strip()))
            #         Speak(int(spl[0].strip()) + int(spl[1].strip()))
            #     except:
            #         try:
            #             spl = rplc.split("-")
            #             print(int(spl[0].strip()) - int(spl[1].strip()))
            #             Speak(int(spl[0].strip()) - int(spl[1].strip()))
            #         except:
            #             try:
            #                 spl = rplc.split("*")
            #                 print(int(spl[0].strip()) * int(spl[1].strip()))
            #                 Speak(int(spl[0].strip()) * int(spl[1].strip()))
            #             except:
            #                 try:
            #                     spl = rplc.split("/")
            #                     print(int(spl[0].strip()) / int(spl[1].strip()))
            #                     Speak(int(spl[0].strip()) / int(spl[1].strip()))
            #                 except:
            #                     Speak("invalid operator")
            
            elif 'generate a image of' in  self.audio:
                sp = self.audio.split('generate a image of')
                self.Speak("generating a image of" + " " + sp)
                response = openai.Image.create(
                prompt=sp[1],
                n=1,
                size="1024x1024"
                )
                image_url = response['data'][0]['url']
                print(image_url)
            
            elif "who is" in self.audio:
                rplce = self.audio.replace("who is","")
                self.Speak(wikipedia.summary(rplce,sentences=1))
                print(wikipedia.summary(rplce))
            
            elif 'music please' in self.audio:
                webbrowser.open("https://www.youtube.com/watch?v=Y633472KofU")

            elif "None" in self.audio:
                pass

            elif 'read pdf' in self.audio:
                import PyPDF2
                doc = open("py.pdf","rb")
                reader = PyPDF2.PdfFileReader(doc)
                pages = reader.numPages
                page = reader.getPage(2)
                text = page.extractText()
                self.Speak(text)
                print(text)

            elif 'send a update message' in self.audio:
                requests.post("https://maker.ifttt.com/trigger/post/json/with/key/kgtZ4Ov5dW0BEfkO0pn75xw7YLvCXfn2ZJh3uSb3RCS")
            
            elif 'send a emergency' in self.audio:
                auth_token = 'b16a2fcc9e64602b4174990a5d93234b' 
                from twilio.rest import Client 
    
                account_sid = 'AC7db82d592d4d2c3a2d99e42d8a256d72' 
                client = Client(account_sid, auth_token) 
                
                message = client.messages.create(         
                                            to='+919958450057',
                                            body="help me!",
                                            from_="+13466448654"
                                        ) 
                
                print(message.sid)
            
            elif 'open camera' in self.audio:
                self.Speak("opening camera")
                vid = cv2.VideoCapture(0)

                while(True):
                    ret, frame = vid.read()
                    cv2.imshow('frame', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                vid.release()
                cv2.destroyAllWindows()

            else:
                self.GetReply(self.audio)

m = Jarvis()
# execu.main()

class Ui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        timer = QTimer(self)
        timer.timeout.connect(self.changeText)
        timer.start(100)
        m.start()


    def changeText(self):
        if g()!="None":
            self.ui.label_2.setText(g())
        else:
            pass
        
    


app = QApplication(sys.argv)
mark = Ui()
mark.show()
sys.exit(app.exec_())