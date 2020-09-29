




import speech_recognition as sr  
import playsound    
from gtts import gTTS   
import os  
import wolframalpha 
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
from io import BytesIO
from io import StringIO
import wikipedia 
import webbrowser
import pyttsx3
import datetime



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)




def speak(audio):
    print("Larry :",audio)
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()





def takeCommand():
    # takes my command from microphone and gives text
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,phrase_time_limit=5)
    print("Stop.")



    try:
        print("recognizing...")
        query = r.recognize_google(audio, language ='en-US')
        print("user said : ", query)
        return query



    except Exception as e:


        print(e)
        speak("Sorry, can you repeat that again?")
        return "None"
    





def search_web(input):
   
    if 'youtube' in input.lower():
        speak("Opening in youtube")
        indx = input.lower().split().index('youtube')
        query = input.split()[indx+1:]
        webbrowser.open("http://www.youtube.com/results?search_query=" + '+'.join(query))  
        return




    elif 'open wikipedia' in input.lower():
        speak("Opening Wikipedia")
        indx = input.lower().split().index('wikipedia')
        query = input.split()[indx + 1:]
        webbrowser.open("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return




    elif 'search on wikipedia' in input.lower():
                speak("Opening Wikipedia")
                
                indx = input.lower().split().index('wikipedia')
                query = input.split()[indx + 1:]
                results = wikipedia.summary(query, sentences = 2)
                speak("According to wikipedia")
                #print(results)
                speak(results)



        
    else:
        if 'google' in input:
            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            webbrowser.open("https://www.google.com/search?q=" + '+'.join(query))
        elif 'search' in input:
            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            webbrowser.open("https://www.google.com/search?q=" + '+'.join(query))
        else:
            webbrowser.open("https://www.google.com/search?q=" + '+'.join(input.split()))
        return







def open_application(input):
    if "chrome" in input:
        speak("Google Chrome")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        return



    elif "word" in input:
        speak("Opening Microsoft Word")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Word 2013')
        return



    elif "excel" in input:
        speak("Opening Microsoft Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Excel 2013')
        return



    
    else:
        speak("Application not available")
        return







def process_text(input):
    try:
        if "who are you" in input or "define yourself" in input:
            spe = '''Hello, I am Larry. Your personal Assistant.
            I am here to make your life easier. 
            You can command me to perform various tasks such as calculating sums or opening applications etcetra'''
            speak(spe)
            return



        elif "who made you" in input or "created you" in input:
            spe = "I have been created by Monish and Shrishti."
            speak(spe)
            return



        elif "crazy" in input:
            spe = """Well, there are 2 mental asylums in India."""
            speak(spe)
            return



        elif "calculate" in input.lower():
            app_id= "E46YXW-T5LG6RT7K7"
            client = wolframalpha.Client(app_id)

            indx = input.lower().split().index('calculate')
            query = input.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            speak("The answer is " + answer)
            return



        elif 'open' in input :
            open_application(input.lower())
            return



        elif 'search' in input or 'play' in input:
            search_web(input.lower())
            return



        elif 'music' in input:
            music_dir = 'F:\Latest'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("music is being played")



        elif 'time' in input:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")



        else:
            speak("I can search the web for you, Do you want to continue?")
            ans = takeCommand()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                search_web(input)
            else:
                return

                
    except Exception as e:
        print(e)
        speak("I don't understand, I can search the web for you, Do you want to continue?")
        ans = takeCommand()
        if 'yes' in str(ans) or 'yeah' in str(ans):
            search_web(input)







if __name__ == "__main__":
    
    name ='Human'
    
    speak("Hello, " + name + '.')
    while(1):
        speak("What can i do for you?")
        text = takeCommand().lower()
        
        if text == 0:
            continue
        
        if "exit" in str(text) or "bye" in str(text) or "go " in str(text) or "sleep" in str(text):
            speak("Ok bye, "+ name+'.')
            break
        process_text(text)

