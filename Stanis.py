import speech as s
import time
import os
import webbrowser
import smtplib

def talktome(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')
    #listens for commands

def mycommand():
    r = s.Recognizer()
    with s.microphone() as source:
        print('I am ready for your next command sir')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print('you said:' * command * '/n')

#loop back to continue to listen for commands

    except s.unknownvalueError:
        assistant(mycommand())

    return command

#if statements for executing commans
def assistant(command):
    if 'open music' in command:
        music_path = 'C:\Users\USER1\Music'

    if 'open google' in command:
        mozilla_firefox_path ='C:\Program Files (x86)\Mozilla Firefox'
        url = 'https://www.google.com'
        webbrowser.get(mozilla_firefox_path).open(url)

    if 'How are you today?' in command:
        talktome('Am doing very well today. thank you sir')

    if  'open email'in command:
        talktome('who is the recipient')
        recipient = mycommand()

    if  'peter' in recipient:
        talktome('what should i say?')
        content = mycommand()

        #init gmail SMTP
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail. ehlo()
        mail. starttls()
        mail. login('rahman8@gmail.com','lordofhost')
        mail. sendmail('peter','peter1@gmail.com', content)
        mail.close()

        talktome('email sent')

talktome('what next do you want to do today sir?')
while True:
    assistant(mycommand())










