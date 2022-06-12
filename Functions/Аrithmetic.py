import pyttsx3

def say(answer):
    """
    function for voice
    """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if voice.name == "Microsoft Zira Desktop - English (United States)":
            engine.setProperty('voice', voice.id)
    engine.say(answer)
    engine.runAndWait()


def plus_f(string):
    say(int(string[0]) + int(string[2]))


def minus_f(string):
    say(int(string[0]) - int(string[2]))


def ymn_f(string):
    say(int(string[0]) * int(string[2]))


def del_f(string):
    say(int(string[0]) / int(string[2]))


def operation(string):
    """
    this function distributes data in functions
    To get the result, you must follow the following notation: "number one" + "operation" + "number two"
    """
    try:
        string = string.split()[1:]
        if "+" == string[1]:   # plus
            plus_f(string)

        elif "-" == string[1]:  # minus
            minus_f(string)

        elif "/" == string[1]:  # division
            del_f(string)

        elif "х" == string[1]:  # multiplication
            ymn_f(string)
    except Exception as ex:
        print("fail :"+ex)
