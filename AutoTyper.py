from pynput.keyboard import Key, Controller, Listener
import time
# Made by yours truly, Edgelord - Edgelord#1214

keyboard = Controller()
print('Filename for testimony please. No .txt needed. \n')
filename = input() + '.txt'
lines = []
n = -1
limit = 0
print(' Press up for next statement, down for previous, left for auto type, and right to repeat statement.\n You can press home to set(in console) statement.\n')
with open(filename, errors="ignore") as f:
    while True:
      line = f.readline()
      if not line:
          break
      encoded_string = line.encode("ascii", "ignore")
      decode_string = encoded_string.decode()
      lines.append(decode_string)
      limit = limit + 1
def on_press(key):
    #print('{0} pressed'.format(
        #key))
    check_key(key)

def on_release(key):
    #print('{0} release'.format(
       # key))
    if key == Key.esc:
        # Stop listener
        return False

def check_key(key):
    if key in [Key.up]:
        global Witness_Testimony
        global n
        n = n + 1 
        keyboard.type(lines[n])
        keyboard.press(Key.enter)
    elif key in [Key.down]:
        n = n - 1
        keyboard.type(lines[n])
        keyboard.press(Key.enter)
    elif key in [Key.right]:
        keyboard.type(lines[n])
    elif key in [Key.home]:
        while True:
            try:
                n = int(input('Type in a number.\n'))
                n = n - 2
                break
            except ValueError:
                print("Not a number, dude.")
        
    elif key in [Key.left]:
        j = 0
        n = -1
        while True:
            n = n + 1
            keyboard.type(lines[n])
            keyboard.press(Key.enter)
            j = j + 1
            if j == limit:
                keyboard.press(Key.enter)
                n = -1
                time.sleep(3 + len(lines[n])/15)
                break
            time.sleep(3 + len(lines[n])/15)


# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
