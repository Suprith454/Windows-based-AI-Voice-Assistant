from datetime import datetime
from speech.speak import speak

def tell_time():
    time = datetime.now().strftime("%I:%M %p")
    speak(f"The time is {time}")
