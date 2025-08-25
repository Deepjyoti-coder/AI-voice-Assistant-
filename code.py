# AI Voice Assistant in Python

# Install required libraries before running:
# pip install SpeechRecognition
# pip install pyttsx3
# pip install pywhatkit
# pip install wikipedia

import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime

# Text to speech function
def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # 0 for male, 1 for female
    engine.say(command)
    engine.runAndWait()

# Capture voice commands
def commands():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("listening...")
            audio = r.listen(source)
            mytext = r.recognize_google(audio)
            mytext = mytext.lower()
            print(mytext)

            # Recognize and respond to different commands
            if 'play' in mytext:
                mytext = mytext.replace('play', '')
                speak('playing ' + mytext)
                pywhatkit.playonyt(mytext)
            elif 'date' in mytext:
                today = datetime.date.today()
                speak(str(today))
            elif 'time' in mytext:
                time = datetime.datetime.now().strftime('%H:%M')
                speak("Time now is " + time)
            elif 'who is' in mytext:
                person = mytext.replace('who is', '')
                info = wikipedia.summary(person, 1)
                speak(info)
            elif 'phone number' in mytext:
                phone_numbers = {'ravi':'1234567890','raja':'9876543210','kumar':'9827341122'}
                names = list(phone_numbers)
                for name in names:
                    if name in mytext:
                        speak(name + " phone number is " + phone_numbers[name])
            elif 'account number' in mytext:
                bank_accounts = {'ttd':'123456789','mm':'9999-33-399'}
                banks = list(bank_accounts)
                for bank in banks:
                    if bank in mytext:
                        speak(bank + " bank account number is " + bank_accounts[bank])
            elif 'tell about' in mytext:
                topic = mytext.replace('tell about', '')
                info = wikipedia.summary(topic, 1)
                speak(info)
            else:
                speak("Please ask a correct question.")
                
    except Exception as e:
        print(e)
        speak("Error in capturing, please speak again.")

# Main function to keep running the assistant
while True:
    commands()
