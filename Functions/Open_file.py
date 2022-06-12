import os
import pyttsx3

def open_f(string):
    """
    open programs from a folder of your choice
    to call you need to say open the program
    """
    name = ' '.join(string.split()[2:])
    try:
        arr = os.listdir("C:\\file_for_open\\")     # folder for searching blanks for quick start
        for i in range(len(arr)):                   # to search, it is enough to name the file name without format
            if name.title() in arr[i] or name.lower() in arr[i] or name.upper() in arr[i]:
                name ="C:\\file_for_open\\" + arr[i]
        os.system("start "+name)

    except FileNotFoundError:
        tts = pyttsx3.init()
        tts.say('Файл не найден')
        tts.runAndWait()
