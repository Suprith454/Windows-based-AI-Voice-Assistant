import os
from speech.speak import speak

def open_app(command):
    if "notepad" in command:
        speak("Opening Notepad")
        os.startfile("notepad.exe")

    elif "calculator" in command:
        speak("Opening Calculator")
        os.startfile("calc.exe")

    elif "chrome" in command:
        speak("Opening Google Chrome")
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    else:
        speak("Application not found")
