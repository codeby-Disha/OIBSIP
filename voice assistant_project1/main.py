import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import sys

# --- Initialization Function ---
def init_engine():
    try:
        # Initializing without 'sapi5' explicitly can improve compatibility
        engine = pyttsx3.init() 
        voices = engine.getProperty('voices')
        
        # Check if voices exist before setting property
        if voices:
            engine.setProperty('voice', voices[0].id)
        
        engine.setProperty('rate', 190)
        return engine
    except Exception as e:
        print(f"Error initializing Voice Engine: {e}")
        return None

engine = init_engine()

def speak(audio):
    """Prints and speaks the input text"""
    print(f"Assistant: {audio}")
    if engine:
        # This prevents the "runAndWait already running" error
        if engine._inLoop:
            engine.endLoop()
            
        engine.say(audio)
        engine.runAndWait()
    else:
        print("Speech engine not available.")

def takeCommand():
    """Main listening function using Google Speech Recognition"""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold = 0.6
        # Quick adjustment for background noise
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        print("\nListening...")
        
        try:
            # Listen for 5 seconds total, max 5 seconds per phrase
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            return "none"
        except sr.RequestError:
            print("Network error. Check your internet.")
            return "none"
        except Exception:
            return "none"

if __name__ == "__main__":
    if engine:
        speak("Hi, your Assistant is here. Ready for your command.")
    else:
        print("Voice system failed to start. Running in text-only mode.")

    while True:
        query = takeCommand()

        # --- SEARCH LOGIC ---
        if 'search' in query:
            speak("What do you want to search for?")
            search_query = takeCommand()
            
            if search_query != "none":
                speak(f"Searching for {search_query}")
                webbrowser.open(f"https://www.google.com/search?q={search_query}")
            else:
                speak("I didn't catch that. Search cancelled.")

        # --- TIME LOGIC ---
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"It's {strTime}")

        # --- DATE LOGIC ---
        elif 'date' in query:
            today = datetime.date.today().strftime("%B %d")
            speak(f"Today is {today}")

        # --- EXIT LOGIC ---
        elif 'exit' in query or 'stop' in query:
            speak("Goodbye")
            # Break the loop to stop the program
            break