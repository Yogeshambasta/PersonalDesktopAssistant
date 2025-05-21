# 1. Importing Required Modules
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
# Text-to-Speech
def say(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()
# Voice Recognition
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            return data.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return "None"
        except sr.RequestError:
            print("Network error.")
            return "None"
# Command Processing
def process_command(command):
    if "open youtube" in command:
        say("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        say("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open notepad" in command:
        say("Opening Notepad")
        os.system("notepad")

    elif "open calculator" in command:
        say("Opening Calculator")
        os.system("calc")

    elif "time" in command:
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M %p")
        say(f"The current time is {current_time}")

    elif "open spotify" in command:
        say("opening spotify")
        os.system("spotify")

    elif command:
        say("You said " + command)
    else:
        say("Sorry, I didn't catch that.")


say("Hello, I am peter A.I. How can I help you?")
command = speech_to_text()
process_command(command)
