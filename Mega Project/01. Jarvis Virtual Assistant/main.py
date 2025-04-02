# import speech_recognition as sr
# import webbrowser
# import pyttsx3
# import musicLibrary
# import moviesLibrary

# # Initialize recognizer and text-to-speech engine
# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# def speak(text):
#     """Converts text to speech."""
#     engine.say(text)
#     engine.runAndWait()

# def processCommand(c):
#     """Processes user commands."""
#     c = c.lower()  # Convert to lowercase for case insensitivity
    
#     if "open google" in c:
#         speak("Opening Google")
#         webbrowser.open("https://google.com")

#     elif "open facebook" in c:
#         speak("Opening Facebook")
#         webbrowser.open("https://facebook.com")

#     elif "open youtube" in c:
#         speak("Opening YouTube")
#         webbrowser.open("https://youtube.com")

#     elif "open amazon" in c:
#         speak("Opening Amazon")
#         webbrowser.open("https://amazon.com")

#     elif "open gmail" in c:
#         speak("Opening Gmail")
#         webbrowser.open("https://gmail.com")

#     elif "open netflix" in c:
#         speak("Opening Netflix")
#         webbrowser.open("https://netflix.com")

#     elif c.startswith("play"):
#         song = c.lower().split(" ")[1]
#         link = musicLibrary.music[song]
#         webbrowser.open(link)

#     elif c.startswith("watch"):
#         movie = c.lower().split(" ")[1]
#         link = moviesLibrary.movies[movie]
#         webbrowser.open(link)


#     elif "exit" in c or "quit" in c:
#         speak("Goodbye!")
#         exit()

#     else:
#         speak("Sorry, I didn't understand that command.")

# if __name__ == "__main__":
#     speak("Initializing Jarvis.....")
    
#     while True:
#         try:
#             with sr.Microphone() as source:
#                 print("Listening for 'Jarvis'...")
#                 recognizer.adjust_for_ambient_noise(source)  # Helps reduce background noise
#                 audio = recognizer.listen(source, timeout=5, phrase_time_limit=2)

#                 word = recognizer.recognize_google(audio).lower()
#                 print(f"Heard: {word}")

#                 if word == "jarvis":
#                     speak("Yes?")
#                     print("Jarvis Activated... Speak a command!")

#                     with sr.Microphone() as source:
#                         recognizer.adjust_for_ambient_noise(source)
#                         audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)

#                     command = recognizer.recognize_google(audio)
#                     print(f"Command: {command}")

#                     processCommand(command)

#         except sr.UnknownValueError:
#             print("Could not understand audio.")
#         except sr.RequestError:
#             print("Could not request results from Google Speech Recognition.")
#         except Exception as e:
#             print(f"Error: {e}")


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

def open_website(url, name):
    """Opens a specified website and announces it."""
    speak(f"Opening {name}")
    webbrowser.open(url)

def processCommand(command):
    """Processes user commands for Jarvis."""
    command = command.lower()  # Convert to lowercase for consistency

    # Dictionary mapping commands to their respective actions
    command_map = {
        "open google": ("https://google.com", "Google"),
        "open facebook": ("https://facebook.com", "Facebook"),
        "open youtube": ("https://youtube.com", "YouTube"),
        "open amazon": ("https://amazon.com", "Amazon"),
        "open gmail": ("https://gmail.com", "Gmail"),
        "open netflix": ("https://netflix.com", "Netflix"),
    }

    # Check if the command matches a website command
    for key in command_map:
        if key in command:
            open_website(*command_map[key])
            return

    # Handle music and movie playback
    if command.startswith("play"):
        song = command.split(" ", 1)[1]  # Extract song name
        if song in musicLibrary.music:
            webbrowser.open(musicLibrary.music[song])
            speak(f"Playing {song}")
        else:
            speak("Sorry, I couldn't find that song.")

    elif command.startswith("watch"):
        movie = command.split(" ", 1)[1]  # Extract movie name
        if movie in moviesLibrary.movies:
            webbrowser.open(moviesLibrary.movies[movie])
            speak(f"Playing {movie}")
        else:
            speak("Sorry, I couldn't find that movie.")

    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I didn't understand that command.")

def listen():
    """Listens for a command and returns recognized text."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        print("Listening...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)
    
    try:
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    
    while True:
        print("Say 'Jarvis' to activate.")
        wake_word = listen()

        if wake_word == "jarvis":
            speak("Yes?")
            command = listen()
            if command:
                processCommand(command)
