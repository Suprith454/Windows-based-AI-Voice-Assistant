from skills.time_date import tell_time
from skills.open_apps import open_app

def handle_command(command):
    if "time" in command:
        tell_time()
        return True

    if "open" in command:
        open_app(command)
        return True

    return False
