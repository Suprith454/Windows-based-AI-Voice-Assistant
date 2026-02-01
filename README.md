## Windows AI Voice Assistant (Python)

A native **Windows-based AI Voice Assistant** built using Python.  
It listens to voice commands, performs system-level actions, and responds using offline text-to-speech.

---------------------------------------------------------------------------------------

## Features
-  Voice command recognition
-  Offline text-to-speech (no internet needed for speaking)
-  Open Windows applications (Notepad, Calculator, Chrome)
-  Tell current time
-  Wake-word based activation
-  Modular and scalable architecture

---------------------------------------------------------------------------------------

## Tech Stack
- **Python 3.11**
- **SpeechRecognition**
- **PyAudio**
- **pyttsx3**
- Windows OS

---------------------------------------------------------------------------------------

## Project Structure

AI_Assistant/
│
|── assistant.py
│
|── speech/
│ |── listen.py
│ |── speak.py
│
|── skills/
│ |── router.py
│ |── open_apps.py
│ |── time_date.py
│
|── requirements.txt
|── README.md

---------------------------------------------------------------------------------------

## Installation & Setup (Windows)

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

---------------------------------------------------------------------------------------

## Clone the repository
```bash
git clone https://github.com/your-username/AI_Assistant.git
cd AI_Assistant

---------------------------------------------------------------------------------------

## Clone the repository

python assistant.py

---------------------------------------------------------------------------------------

## How It Works

- Captures voice input via microphone

- Converts speech to text

- Matches command using a router module

- Executes system-level tasks

- Responds using offline TTS

---------------------------------------------------------------------------------------

## Use Cases

- AI / Python learning project

- Voice automation demo

---------------------------------------------------------------------------------------

## Future Enhancements

- ChatGPT / LLM integration

- Desktop GUI (Tkinter)

- Email automation

- File search

- Memory & personalization

---------------------------------------------------------------------------------------

## Author

Suprith M
Artificial Intelligence & Data Science Student