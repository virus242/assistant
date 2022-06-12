import pyttsx3
import random


def rand_nom():
    """
    random number
    to get a random number you need to say "random number"
    """
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        for voice in voices:
            if voice.name == "Microsoft Zira Desktop - English (United States)":
                engine.setProperty('voice', voice.id)
        engine.say(random.randint(0, 100))
        engine.runAndWait()

    except Exception as ex:
        print("fail :"+ex)
