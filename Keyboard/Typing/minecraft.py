from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

text = input("Text: ")
amount = input("How many time will it loop? ")
amount = int(amount)

time.sleep(5)
for i in range(amount):
    keyboard.press('t')
    keyboard.release('t')
    time.sleep(0.5)
    keyboard.type(text)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)
