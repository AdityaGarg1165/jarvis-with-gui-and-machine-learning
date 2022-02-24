import winsound
import datetime
import speech_recognition as sr

inp = int(input("time bata h"))
inp2 = int(input("time bata m"))



while True:
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute




    if inp == hour and minute == inp2:
        winsound.PlaySound("SystemQuestion",winsound.SND_LOOP)
    elif inp > hour or minute > inp2:
        break