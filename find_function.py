"""
This module is needed to
find a function on request
"""

import Functions.Open_file as FOpen
import Functions.Time_now as FTime
import Functions.Date as FDate
import Functions.Notes as FNotes
import Functions.rand_nom as FRand
import Functions.PC as FPc
import Functions.Аrithmetic as FArif


def find_function(string):
    """this function distributes the user's
    request to the desired functions"""
    print(string)
    try:
        if "open file" in string.lower() or "открой файл" in string:  # function to open a file
            FOpen.open_f(string)                                      # to call say "open file"

        elif "time" in string.lower() or "время" in string.lower():  # function to call the function of working with time
            FTime.time_now()                                         # to call say "What time is it now"

        elif "date" in string.lower() or "дата" in string.lower():  # function call for date
            FDate.date_now_f(string)

        elif "add note" in string.lower() or "добавить заметку" in string.lower():  # add notes
            FNotes.Add_node(string)

        elif "read note" in string.lower() or "читать заметки" in string.lower():   # read notes
            FNotes.read_nodes()

        elif "random number" in string.lower() or "случайное число" in string.lower():  # get a random number
            FRand.rand_nom()

        elif "turn off computer" in string.lower() or "выключи компьютер" in string.lower():    # turn off computer
            FPc.ps_off()

        elif "restart computer" in string.lower() or "перезагрузи компьютер" in string.lower():     # to restart a computer
            FPc.reb_pc()

        elif "count" in string.lower() or "посчитай" in string.lower():     # call arithmetic functions
            FArif.operation(string)
    except Exception as ex:
        print("fail :" + ex)