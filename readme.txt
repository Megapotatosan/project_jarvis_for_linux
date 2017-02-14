***************
****read_me****
***************

ProjectJarvis is Python based Speech Interpretation and Recognition application for linux system

Required Packages:
pyttsx - for converting text into speech so that the application will speak out the command.
		(if you are using python 3 or above,ensure that that install pyttsx1.1)

speechrecognition - Library for performing speech recognition, with support for several engines and APIs, online and offline.

pyowm -  A Python wrapper around the OpenWeatherMap web API

how to use:
ProjectJarvis is a CLI application, if you want to start up this application,
you should run it in the terminal or python IDE
1.after starting up,Jarvis will ask for the command.
2.when "Say something!" occured, user can input command by vocal
3.after Jarvis listen the command, the command will convert from speech into text by the Speech Recognition engine
4.and the text command would be stored as a string and pass to main function :def Jarvis(data_google,data_wit) 