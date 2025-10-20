import os
import random
import time
import sys


cursorList = "C://" #path to config file
skinsDir =  "C://" #path to osu skin folder, NOT the skin itself
skinFolder = ""


skin = ""
previous = ""
lines = []
cursors = []


with open(cursorList, "r") as file:
    try:
        lines = file.readlines()
    except FileNotFoundError:
        print("List file was not located.")
    except Exception as e:
        print("There was an error loading the list file.")
       


for a in range(0, lines.__len__()):
    if lines[a].startswith("--"):
        line = lines[a].removeprefix("--")
        cursors.append(line.removesuffix("\n"))
    elif lines[a].startswith("++"):
        line = lines[a].removeprefix("++")
        previous = line.removesuffix("\n")
    elif lines[a].startswith("==") and not(lines[a].__contains__("C:")):
        line = lines[a].removeprefix("==")
        skin = line.removesuffix("\n")
    elif lines[a].startswith("==C:"):
        line = lines[a].removeprefix("==")
        skinsDir = line.removesuffix("\n")
try:
    skinFolder = os.path.join(skinsDir, skin)
except Exception as e:
    print("There was an error creating the path.")


num = random.randint(0, cursors.__len__() - 1)


oldName = os.path.join(skinFolder, cursors[num])
altName = os.path.join(skinFolder, "x.png")
cursorName = os.path.join(skinFolder, "cursor.png")


try:
    os.rename(oldName, altName)
    os.rename(cursorName, oldName)
    previous = cursors[num]
    os.rename(altName, cursorName)
except Exception as e:
    print("There was an error changing names.")
    print(e)


with open(cursorList, "w") as file:
    try:
        file.write("")
    except FileNotFoundError:
        print("List file was not located.")
    except Exception as e:
        print("There was an error writing to the list file.")


with open(cursorList, "a") as file:
    for b in range(0, lines.__len__()):
        try:
            if lines[b].startswith("++"):
                file.write("++" + previous)
            else:
                file.write(lines[b])
        except FileNotFoundError:
            print("List file was not located.")
        except Exception as e:
            print("There was an error writing to the list file.")
   
print("Cursor Randomized")
time.sleep(.5)

