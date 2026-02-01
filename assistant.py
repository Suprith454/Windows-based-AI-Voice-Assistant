from speech.listen import listen
from speech.speak import speak
from skills.router import handle_command

WAKE_WORD = "assistant"

speak("Hello, I am your Suprith. How can i help you.")

while True:
    command = listen()

    if not command:
        continue

    # Wake word handling
    if WAKE_WORD in command:
        command = command.replace(WAKE_WORD, "").strip()

    if "exit" in command or "quit" in command or "bye" in command:
        speak("Bye, You are always welcome!")
        break

    handled = handle_command(command)

    if not handled:
        speak("Sorry, I did not understand your command")
