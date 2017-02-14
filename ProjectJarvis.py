#build by mingH 06/12/2016 01:00
import speech_recognition as sr
from datetime import datetime
import pyttsx
import os
import time
import pyowm
import re

#set up the text to speech engine
engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
engine.setProperty('voice', 1)
#openweathermap_API
owmAPI_key = '01ac0d6eccb4b34fc0e9ee925ac40a3d'
owm = pyowm.OWM(owmAPI_key)

#wit.ai API key
WIT_AI_KEY = "OC2V5HEAAMKYTG6G2UJDE2BRHJKGM6U6" # Wit.ai keys are 32-character uppercase alphanumeric strings
#
complement = ["thank","good","great","awesome"]
days_keyword = ["today","yesterday","tomorrow","next week","last week"]
weather_keyword = ["snow","umbrella","cold","hot","rain","sunny","weather"]
location_keyword = ["Taiwan","Hong Kong","Japan","Korea"]
def speak(text):
     engine.say(text)
     engine.runAndWait()

def Recognize():
    #set up Recognizer
    r = sr.Recognizer()
    r.energy_threshold = 3000
    with sr.Microphone(sample_rate = 16000, chunk_size = 1024) as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)


    #multirecognizer to improve accuracy
    #data1 = ""
    data2 = ""
    data3 = ""
    #rubbish  
    #try:
    #    print("Sphinx thinks you said " + r.recognize_sphinx(audio))    
    #    data1 = r.recognize_sphinx(audio)
    #except sr.UnknownValueError:
    #    print("Sphinx could not understand audio")
    #except sr.RequestError as e:
    #    print("Sphinx error; {0}".format(e))

    #Google Speech Recognition
    try:
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        data2 = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    #Wit.ai    
    try:
        print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
        data3 = r.recognize_wit(audio, key=WIT_AI_KEY)
    except sr.UnknownValueError:
        print("Wit.ai could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Wit.ai service; {0}".format(e))       
    return data2,data3   

def Jarvis(data_google,data_wit):
    #ask for time
    if("time" in data_google or "time" in data_wit ):
        now = datetime.now()
        speak("the time now is"+str(now.hour)+"o'clock"+str(now.minute))
    #google search
    if("google" in data_google or "google" in data_wit and "search" in data_google or "search" in data_wit):
        data = data_google.split()
        data = data[2:]
        vocal = ' '.join(str(command) for command in data)
        print(vocal)
        speak("let me help you to find out what is" + vocal)
        command = ''.join(str(command) for command in data)
        os.system("google-chrome-stable https://www.google.com.tw/search?q="+command)
    #ask for weather_alpha
    for i in weather_keyword:
        if(i in data_google or i in data_wit):
            print(i)
            #today blablabla
            for x in location_keyword:
                if(x in data_google or x in data_wit):
                    print(x)
                    observation = owm.weather_at_place(x)
                    w = observation.get_weather()
                    temperaturerinfo = w.get_temperature('celsius')
                    weatherinfo = w.get_forecast
                    print(weatherinfo)
                    print(temperatureinfo)
                    temp = re.search("(?<='temp': )\w+",str(temperatureinfo))
                    
                    print(x+" is now "+temp.group(0)+" degree celsius")
                    speak(x+" is now "+temp.group(0)+" degree celsius")
    #command open
    if("open" in data_google or "open" in data_wit):
        if("open" in data_google):
            data = data_google.split()
            data = data[1:]
            command = ''.join(str(command) for command in data)
            print(command.lower())
            os.system(command.lower())
    #shutdown
    if("good bye" in data_google or "good bye" in data_wit):
        speak("see you later!")
        exit(0)
            
            
#init
time.sleep(2)
speak("hello,what can I help you?")
while 1:
    (data_google,data_wit) = Recognize()
    print(" "+str(data_google)+" "+str(data_wit))
    Jarvis(data_google,data_wit)

