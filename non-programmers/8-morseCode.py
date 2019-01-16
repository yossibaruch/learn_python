print("""
# Create a dictionary of morse code and a-z letters
# Get input from user in text (spaces will be truncated) and transform it to morse code
# you might need to lowercase the input
""")
morseCode = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- " \
            "--.."
characterA2B = "abcdefghijklmnopqrstuvwxyz"

dictMorse = dict(zip(str(characterA2B), morseCode.split(" ")))

while True:
    try:
        text2Morse = input("Please enter the strings you want to translate to morse code (a-z with spaces):")
    except ValueError:
        print("This I can not print, try again")
        continue
    break

for string in list(text2Morse.lower()):
    if ' ' not in string:
        print(dictMorse[string], " ", end='')
    else:
        print("")
