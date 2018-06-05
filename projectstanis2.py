
import pyaudio
import pyttsx3
import speech_recognition as sr
import time
import os
import webbrowser
import smtplib
import sphinx
engine = pyttsx3.init()

engine.say("Say something, please.")

def speak():
    engine.say(text)
    engine.runAndWait()

    #listens for commands
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
    try:
        return r.recognize_google(audio) 

#loop back to continue to listen for commands
    except sr.unknownvalueError:
       print('sorry, say again')
    except sr.requesterror as e:
        print('recog errors (0)'.format(e))
    return
def greeting():
    speak('i\'m fine sir, hope you are good too')
    speak('what do you want to do today?')

def chrome():
    os.system('start chrome .exe')
    speak('opening chrome')
    speak('wait a moment sir')
    speak('what would you like to search for today?')
    webbrowser.open_new_tab('http://google.com' + listen())
    speak('OK, searching...')

def music():
    speak('opening music player')
    speak('loading music files')
    speak('wait a moment sir')
    os.system('start windows media player.exe')
    speak('what would you like me to play?')
    os.startfile('C:/Users/USER1/Music/'+listen()+'mp3')
    speak('okay, now playing'+listen()+'for you')


def playlist():
    speak('loading playlist')
    speak('wait a moment sir')
    speak('please choose a song')

def time():
    speak('the time is ' + time)


def email():
    speak('opening email')
    speak('who is the recipient')
    recipient = listen()

def notepad():
    speak('opening notepad')
    speak('what would you like to put down sir?')

    if  'peter' in recipient:
        speak('what should i say?')
        content =listen()

        #init gmail SMTP
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail. ehlo()
        mail. starttls()
        mail. login('rahman8@gmail.com','lordofhost')
        mail. sendmail('peter','peter1@gmail.com', content)
        mail.close()

        engine.say('email sent')

engine.say('what next do you want to do today sir?')


def mainfunction(source):
    r=sr.Recognizer()
    audio=r.listen(source)
    user=r.recognize_sphinx(audio)

    if user =='hello,goodmorning stanis,hello stannis,whats up stanis, how are you stannis, good day stanis, good afternoon stanis, good afternoon':
        greeting()

    elif user =='open chrome,open browser,search':
         chrome()
    elif user == 'open music player, play some music, music':
        windowsmusicplayer()
    elif user == 'email':
        email()
    elif user == 'open notepad, notepad, take this down':
        notepad()

def loop():
    if __name__=="__main__":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            while 1:
                mainfunction(source)

loop()









