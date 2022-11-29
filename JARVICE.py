import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
import smtplib,ssl #use to send the mail
import pywhatkit as pwt
import pyautogui
import time


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()




def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    
    elif hour>=12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening")

    speak("Hello I'M Jarvis Nitish and Vijay Sir, Please Tell Me How can i Help You?")

def takeCommand():
# it take microphone input from the user and returns string output
     r = sr.Recognizer()
     with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("say anything : ")
        audio= r.listen(source)

     try: 
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"user said:{query}\n")
     except Exception as e:
        print("Say that again please...")
        return "None"
     query=query.lower()
     return query

def sendEmail(to,content):
     context=ssl.create_default_context()   
     with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as server:
        server.login('vp0013621@gmail.com', 'jmgqcuzueqiaioxe')
        server.sendmail('vp0013621@gmail.com', to, content)
        
        

if __name__ == "__main__" :
    wishMe()
    while True:
            query = takeCommand()
            # Logic for executing tasks based on query
            if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
                    speak('Searching Wikipedia...')
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2) 
                    speak("According to Wikipedia")
                    print(results)
                    speak(results)
            elif 'open youtube' in query:
                    webbrowser.open("youtube.com")

            elif 'open google' in query:
                    webbrowser.open("google.com")
            elif 'play music' in query:
                    music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                    songs = os.listdir(music_dir)
                    print(songs)    
                    os.startfile(os.path.join(music_dir, songs[0]))
            elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(f"Sir, the time is {strTime}")
            elif 'exit' in query:
                    break
            

            elif 'email' in query:
                        speak("What should I say: ?")
                        content = takeCommand()
                        print("Your massage is \n:  ", content)
                        speak("Enter the reciever Email Id ")
                        to = takeCommand()
                        sendEmail(to,content)
                        speak("Email has been sent!")
            elif 'message' in query:
                
                speak("Enter the whatsapp number")
                no = input()
                no = '+91' + no

                speak("What massage i need to send?, please tell me")
                massage=takeCommand() 
                pwt.sendwhatmsg_instantly(no, massage)
                pyautogui.press('enter')
                input("press Enter key to exit: ")
                break
                

            else:
              webbrowser.open(query)
