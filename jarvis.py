import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[1].id)
engine.setProperty("voice", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you?")

def takeCommand():
    # Its take microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" or "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            music_dir = "D:\\Non Critical\\songs\\Favourite Songs2"
            songs = os.list_dir("music_dir")
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
        elif "open code" in query:
            codePath = "C:\\Users\\cs\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codePath)
        elif "send email" in query:
            email_sender_path = "C:\\Users\\cs\\Desktop\\Code Playground\\Python Projects\\Email Sender\\python_app.py"
            os.startfile(email_sender_path)
        elif "quit" in query:
            exit()