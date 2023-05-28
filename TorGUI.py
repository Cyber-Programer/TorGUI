import subprocess
import sys
import ctypes
from tkinter import *


def start_tor():
    try:
        result = subprocess.run(['tor', '--version'], capture_output=True, text=True)
        output = result.stdout.strip()
        creation_flags = subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0
        subprocess.Popen(['tor'], creationflags=creation_flags)

    except subprocess.CalledProcessError as e:
        subprocess.Popen(['sudo', 'apt', 'install', 'tor', '-y'])


def stop_tor():
    try:
        if sys.platform == 'win32':
            ctypes.windll.user32.EnumWindows.EnumWindows(EnumWindowsProc, os.getpid())
        else:
            subprocess.run(['pkill', 'tor'])

    except subprocess.CalledProcessError as e:
        pass


root = Tk()
root.title('Tor GUI')
root.iconbitmap('Tor.png')

Label(text="Tor GUI", font=('', 16, 'bold')).pack()

x = Frame(root, borderwidth=1, relief="solid")
x.pack(padx=20, pady=50)

btn1 = Button(x, text='START TOR', font=('', 14), width=20, command=start_tor)
btn1.pack(pady=10)

btn2 = Button(x, text='STOP TOR', font=('', 14), width=20, command=stop_tor)
btn2.pack(pady=10)

root.mainloop()
