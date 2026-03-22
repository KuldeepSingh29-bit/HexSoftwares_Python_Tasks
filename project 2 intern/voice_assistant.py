import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from deep_translator import GoogleTranslator

# Initialize the text-to-speech engine
# sapi5 is the Microsoft Speech API built into Windows
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Switch to voices[1].id for a female voice

def speak(audio):
    """Converts text to speech and plays it"""
    print(f"Assistant: {audio}")
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    """Greets the user depending on the current time"""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
        
    speak("I am your personal voice assistant. How may I help you today?")

def take_command():
    """Takes microphone audio from the user and turns it into text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        # Pause threshold controls how long the user can pause before the string is returned
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("I didn't quite catch that. Could you say that again?")  
        return "None"
    
    return query.lower()

def main():
    print("="*45)
    print("           CUSTOM VOICE ASSISTANT")
    print("="*45)
    
    wish_me()
    
    while True:
        query = take_command()
        
        # If couldn't recognize speech, prompt again
        if query == "none":
            continue

        # Task Logic Based on Commands
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                # Get a 2-sentence summary from Wikipedia
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia...")
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There were too many results, please be more specific.")
            except wikipedia.exceptions.PageError as e:
                speak("I could not find a matching page on Wikipedia.")

        elif 'open youtube' in query:
            speak("Opening YouTube in your browser")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Opening Google in your browser")
            webbrowser.open("https://www.google.com")
            
        elif 'time' in query:
            current_time = datetime.datetime.now().strftime("%I:%M %p")    
            speak(f"The current time is {current_time}")

        elif 'translate' in query and 'hindi' in query:
            speak("What would you like me to translate to Hindi?")
            to_translate = take_command()
            if to_translate != "none":
                try:
                    speak("Translating...")
                    translated = GoogleTranslator(source='auto', target='hi').translate(to_translate)
                    print(f"\n--- HINDI TRANSLATION ---\n{translated}\n-------------------------\n")
                    speak("I have printed the Hindi translation on your screen.")
                except Exception as e:
                    speak("Sorry, I encountered an error while translating.")

        elif 'quit' in query or 'exit' in query or 'stop' in query or 'goodbye' in query:
            speak("Goodbye! Have a great day.")
            break
            
        else:
            speak("I heard you, but I am not programmed to handle that command yet.")

if __name__ == "__main__":
    main()
