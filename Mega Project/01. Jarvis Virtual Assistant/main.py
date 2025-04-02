import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import moviesLibrary

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    """Processes user commands."""
    c = c.lower()  # Convert to lowercase for case insensitivity
    
    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open facebook" in c:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open amazon" in c:
        speak("Opening Amazon")
        webbrowser.open("https://amazon.com")

    elif "open gmail" in c:
        speak("Opening Gmail")
        webbrowser.open("https://gmail.com")

    elif "open netflix" in c:
        speak("Opening Netflix")
        webbrowser.open("https://netflix.com")

    elif c.startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif c.startswith("watch"):
        movie = c.lower().split(" ")[1]
        link = moviesLibrary.movies[movie]
        webbrowser.open(link)


    elif "exit" in c or "quit" in c:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for 'Jarvis'...")
                recognizer.adjust_for_ambient_noise(source)  # Helps reduce background noise
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=2)

                word = recognizer.recognize_google(audio).lower()
                print(f"Heard: {word}")

                if word == "jarvis":
                    speak("Yes?")
                    print("Jarvis Activated... Speak a command!")

                    with sr.Microphone() as source:
                        recognizer.adjust_for_ambient_noise(source)
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)

                    command = recognizer.recognize_google(audio)
                    print(f"Command: {command}")

                    processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition.")
        except Exception as e:
            print(f"Error: {e}")


