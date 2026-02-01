Windows AI Voice Assistant (Python)

This project implements a voice assistant on Windows using Python.

Structure:

```
|-- speech/          # Microphone input and TTS
  |-- listen.py      # Speech-to-text
  |-- speak.py       # Text-to-speech
|-- skills/          # Task execution
  |-- router.py      # Command routing
  |-- open_apps.py   # Opens applications
  |-- time_date.py   # Provides time and date
|-- requirements.txt
|-- README.md
```

Installation:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Usage:

1.  Clone the repository:

    ```bash
    git clone https://github.com/Suprith454/AI-Assistance.git
    cd AI_Assistant
    ```
2.  Run:

    ```bash
    python assistant.py
    ```

Functionality:

The assistant captures voice input, converts it to text, routes the command, executes system tasks, and responds using offline TTS.

Applications:

-   AI/Python learning project
-   Voice automation demonstration

Planned Features:

*   ChatGPT/LLM integration
*   Desktop GUI (Tkinter)
*   Email automation
*   File search
*   Memory & personalization
