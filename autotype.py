import pyautogui
import time
from pynput.keyboard import Key, Listener
from getpass import getpass
import sys

WAIT_TIME=3

if len(sys.argv) == 2:
    command = sys.argv[1]

    if command == "s":
        text_to_type = getpass("What text to you want to type? ")

else:
    text_to_type = input("What text to you want to type? ")

def on_press(key):
    pass
    #print(f"{key} pressed")

def on_release(key):
    #print(f"{key} released")
    if key == Key.esc:
        # Stop listener
        return False
    if 'char' in dir(key):
        if key.char == 'p':
            print(f"Gonna type it in {WAIT_TIME} seconds")
            return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
time.sleep(WAIT_TIME)

pyautogui.typewrite(text_to_type)
