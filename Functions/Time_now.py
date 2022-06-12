from datetime import datetime
import pyttsx3


def time_now():
    """
    function to find the time
    to get the time you need to say "time is now"
    """
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        for voice in voices:    # language selection
            if voice.name =="Microsoft Zira Desktop - English (United States)":
                engine.setProperty('voice', voice.id)

        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")

        engine.say(current_time)    # say the answer
        engine.runAndWait()
    except Exception as ex:
        print("fail :"+ex)
