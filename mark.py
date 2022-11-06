import os
import requests
import bs4
import pywikihow
import cv2
import webbrowser
import speech_recognition
import pyttsx3
import datetime
import random
import wikipedia
from modules.neuralnetwork import bag_of_words,load_model,labels,numpy,data,labels,words

# train(1000)
model = load_model("model/model.pth")
r = speech_recognition.Recognizer()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def Speak(text):
    engine.say(text)
    engine.runAndWait()
    print("Mark:",text)
    

def Wish():
    hour = datetime.datetime.now().hour
    if hour >= 12:
        Speak("Good Afternoon , sir , how may i help you")
    if hour <= 12:
        Speak("Good Morning ,  sir , how may i help you")

        

def VoiceRecognition():
    try:
        with speech_recognition.Microphone() as mic:
            r.adjust_for_ambient_noise(mic, duration=0.2)
            r.pause_threshold = 0.5
            audio = r.listen(mic)
            audio = r.recognize_google(audio,language="en-in")
            return str(audio).lower()
    except:
        return ""

if __name__ == "__main__":
    Wish()
    while True:
        # audio = VoiceRecognition()
        audio=input(":")
        if audio == "":
            pass
        else:
            print("You:",audio  )

            if 'what is the time' in audio:
                Speak(f"sir the time is , {datetime.datetime.now().hour}, {datetime.datetime.now().minute}")
            
            elif "open" in audio:
                query = audio.split(" ")
                if query.__len__() == 3:
                    os.system("code")
                if query.__len__() == 2:
                    if query[1] == "chrome":
                        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                    elif query[1] == "spotify":
                        os.system("spotify")
                    elif query[1] == "youtube":
                        webbrowser.open("youtube.com")
                    elif query[1] == "camera":
                        pass
            elif "scan virus" in audio:
                os.system("mrt")

            elif 'wikipedia' in audio:
                user_query = audio
                user_query = user_query.replace("wikipedia",'')
                user_query = user_query.replace("search",'')
                summary = wikipedia.summary(user_query,sentences=2)
                Speak("according to wikipedia")
                Speak(summary)

            elif 'how to do mode' in audio:
                search = VoiceRecognition()
                Speak("what should i search")
                how_to = pywikihow.search_wikihow(search,max_results=1)
                Speak(how_to[0].summary)
            
            elif 'iphone price' in audio:
                html = requests.get("https://www.flipkart.com/apple-iphone-14-blue-128-gb/p/itmdb77f40da6b6d?pid=MOBGHWFHSV7GUFWA&lid=LSTMOBGHWFHSV7GUFWA3AV8J8&marketplace=FLIPKART&q=iphone+14&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=5b7684cd-e8d9-424d-a65e-51996c1b2961.MOBGHWFHSV7GUFWA.SEARCH&ppt=pp&ppn=pp&ssid=1b1fyctw5s0000001667130980153&qH=860f3715b8db08cd")
                htmldata = html.content
                tomato_soup = bs4.BeautifulSoup(htmldata,'html.parser')
                print(tomato_soup.find('div',class_="_30jeq3 _16Jk6d").get_text())
                Speak(tomato_soup.find('div',class_="_30jeq3 _16Jk6d").get_text())



            else:
                results = model.predict([[bag_of_words(audio, words)]])[0]
                results_index = numpy.argmax(results)
                print(results_index)
                print(results)
                tag = labels[results_index]
                print(results[results_index])
                if results[results_index] > 0.83:
                    for tg in data["intents"]:
                        if tg['tag'] == tag:
                            responses = tg['responses']
                            Speak(random.choice(responses))
                else:
                    Speak("Sorry , i didnt get that sir")

        