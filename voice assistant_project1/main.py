import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import urllib.parse
import sys  

# ---------------- SPEAK FUNCTION (STABLE) ----------------
def speak(text):
    print("Assistant:", text)

    engine = pyttsx3.init('sapi5')  # Windows voice engine
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)

    engine.say(text)
    engine.runAndWait()
    engine.stop()

# ---------------- LISTEN FUNCTION ----------------
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 300
        r.pause_threshold = 0.6
        print("Listening...")

        try:
            audio = r.listen(source, timeout=3, phrase_time_limit=5)
            print("Recognizing...")
            return r.recognize_google(audio, language="en-IN").lower()
        except:
            return "none"

# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    speak("Hello. I am ready. How can I help you?")

    waiting_for_search = False  # 🔹 SEARCH STATE MEMORY

    while True:
        command = listen()

        if command == "none":
            continue

        print("User:", command)

        # ---------------- SEARCH STEP 2 ----------------
        if waiting_for_search:
            query = command.strip()

            speak(f"Searching Google for {query}")

            encoded_query = urllib.parse.quote(query)
            url = f"https://www.google.com/search?q={encoded_query}"
            webbrowser.open_new_tab(url)

            waiting_for_search = False
            continue

        # ---------------- TIME ----------------
        if "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")

        # ---------------- DATE ----------------
        elif "date" in command:
            current_date = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's date is {current_date}")

        # ---------------- SEARCH STEP 1 ----------------
        elif "search" in command:
            speak("What do you want to search?")
            waiting_for_search = True

        # ---------------- EXIT ----------------
        elif "exit" in command or "stop" in command or "quit" in command:
            speak("Goodbye. Closing the assistant.")
            sys.exit()

        # ---------------- UNKNOWN ----------------
        else:
            speak("Sorry, I did not understand that.")
