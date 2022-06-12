import os


def ps_off():
    """
    turn off pc
    to do this, you need to say turn off the pc
    """
    try:
        shutdown_command = "shutdown /s /t 00"
        os.system(shutdown_command)
    except Exception as ex:
        print("fail :"+ex)

def reb_pc():
    """
    restart pc
    All you need to do is to restart your PC
    """
    try:
        restart_command = "shutdown /r /t 00"
        os.system(restart_command)
    except Exception as ex:
        print("fail :"+ex)