from click import command
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener=sr.Recognizer()
engine=pyttsx3.init()
#voices=engine.getProperty('voices')
#engine.setProperty('voice',voices[1].id) 
engine.say('I am alexa, what can I do for you?')
engine.runAndWait()
print("Program started")
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
    except Exception as e:
        pass
    return command

def run_alexa():
    while True:
        command = take_command()
        print(command)
        if 'play' in command:
            try:
                song=command.replace('play','')
                talk('playing' + song)
                pywhatkit.playonyt(song)
            except Exception as e:
                  print("Error in play command:",e)
        elif 'time' in command:
            try:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk('Current time is '+time)
            except Exception as e:
                print("Error in time command:",e)
        elif 'who is' in command:
            try:
                person=command.replace('who is','')
                info=wikipedia.summary(person,1)
                print(info)
                talk(info)
            except Exception as e:
                print("Error in who is command:",e)
        elif 'date' in command:
            try:
                talk('Sorry, I have a headache')
            except Exception as e:
                print("Error in date command:",e)
        elif 'are you ok' in command:
            try:
                talk('No, I am not feeling well')
            except Exception as e:
                print("Error in are you ok command:",e)
        elif 'joke' in command:
            try:
                talk(pyjokes.get_joke())
            except Exception as e:
                print("Error in joke command:",e)
        elif command=='stop':
            try:
                talk('Goodbye!')
                break
            except Exception as e:
                print("Error in stop command:",e)
        else:
            try:
                talk('please say the command again.')
            except Exception as e:
                print("Error in else command:",e)

run_alexa()