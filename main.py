import speech_recognition as sr
import pyttsx3
import find_function

def with_mic(r):
    """
    function for reading data from the microphone
    :param r - Recognizer:
    :return void :
    """

    string = ''
    with sr.Microphone(device_index=1) as source:   # speech recognition
        audio = r.listen(source)

    try:
        string = r.recognize_google(audio, language="ru-RU")
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return string

if __name__ == "__main__":
    string = ''
    while 1:
        r = sr.Recognizer()

        string = with_mic(r)

        if string.lower() == "friday" or string.lower() == "пятница":
            tts = pyttsx3.init()
            voices = tts.getProperty('voices')
            for voice in voices:
                if voice.name == "Microsoft Zira Desktop - English (United States)":
                    tts.setProperty('voice', voice.id)
            tts.say('Yes')
            tts.runAndWait()

            string = with_mic(r)

            find_function.find_function(string)

