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
        print("ERROR:", e)
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is '+time)
    elif 'who is' in command:
        person=command.replace('who is','')
        info=wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Sorry, I have a headache')
    elif 'are you okay' in command:
        talk('No, I am not feeling well, because I have a headacheI have to solve everybody\'s problems')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('please say the command again.')

while True:
    run_alexa()