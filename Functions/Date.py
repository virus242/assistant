from datetime import date   # date
import pyttsx3              # voice


def date_now_f(string):
    """
    get today's date
    for this you need to call Friday and say "the date is today"
    """
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        for voice in voices:    # language selection
            if voice.name == "Microsoft Zira Desktop - English (United States)":
                engine.setProperty('voice', voice.id)

        engine.say(date.today())    # say the answer
        engine.runAndWait()
    except Exception as ex:
        print("fail :"+ex)
