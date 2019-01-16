from time import sleep
import winsound

print("""
# Get bpm
# Play a sound once every 60/bpm seconds
""")

while True:
    try:
        bpm = int(input("please enter bpm: (one of 1/2/3/4/5/6/10/12/15/20/30/60"))
    except ValueError:
        print("Erroneous value, please reenter")
        continue
    break

dt = 60 / bpm

count = 0
while True:
    winsound.Beep(2500, 250)
    sleep(dt - 0.25)
    count += 1
    if count == 10:
        break
