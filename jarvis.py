import os
import time  # Importing time module for delays
import speech_recognition as sr
import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Speed of speech
engine.setProperty("volume", 0.9)  # Volume level

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize voice input
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio).lower()
            return command
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand that.")
        except sr.RequestError:
            speak("Sorry, there seems to be a problem with the speech recognition service.")
        except Exception as e:
            speak("An error occurred.")
            print(e)
        return ""

# Function to perform tasks based on the command
def perform_task(command):
    if "open chrome" in command:
        speak("Opening Chrome...")
        os.system("start chrome")  # Command to open Chrome in Windows
    elif "open youtube" in command:
        speak("Opening YouTube...")
        os.system("start chrome https://www.youtube.com")  # Opens YouTube in browser
    elif "open vscode" in command or "open visual studio code" in command:
        speak("Opening Visual Studio Code...")
        os.system("code")  # Assumes 'code' command is in PATH
    else:
        speak("Sorry, I don't know how to do that yet.")

# Main function
def jarvis():
    speak("Hello! I'm Jarvis. How can I assist you?")
    while True:
        command = take_command()
        if "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
        elif command:
            perform_task(command)
        speak("Waiting for 2 minutes before listening again.")
        time.sleep(120)  # Wait for 2 minutes before listening again

# Run the assistant
if __name__ == "__main__":
    jarvis()
