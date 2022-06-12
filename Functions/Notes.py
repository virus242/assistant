import pyttsx3


def Add_node(string):
    """
    add a new note
    to do this, you need to say add a note and say the note itself
    """
    string = string.split(' ')
    try:
        with open("Functions/notes/note.txt", 'a', encoding="utf-8") as file:   # writing to file
            file.write(' '.join(string[2:]) + '\n')
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        for voice in voices:    # language selection
            if voice.name == "Microsoft Zira Desktop - English (United States)":
                engine.setProperty('voice', voice.id)
        engine.say('ready')     # say the answer
        engine.runAndWait()
    except Exception as ex:
        print("fail :" + ex)


def read_nodes():
    """
    reading from a file
    to call you need to say read notes
    """
    try:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        for voice in voices:    # language selection
            if voice.name == "Microsoft Zira Desktop - English (United States)":
                engine.setProperty('voice', voice.id)

        with open("Functions/notes/note.txt") as file: # reading from a file

            engine.say(file.read())     # say the answer
            engine.runAndWait()
    except Exception as ex:
        print("fail :"+ex)
