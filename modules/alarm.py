import winsound
import datetime
import speech_recognition as sr

inp = int(input("time bata h"))
inp2 = int(input("time bata m"))

def TakeCommand():
        r = sr.Recognizer()

        with sr.Microphone() as source:
            r.pause_threeshold = 1
            audio = r.listen(source)
        try:
            query = r.recognize_google(audio,language="en-in")
            return query.lower()
        except:
            return "None"


while True:
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute


    if inp == hour and minute == inp2:
        winsound.PlaySound("SystemQuestion",winsound.SND_LOOP)

    elif inp > hour or minute > inp2:
        break