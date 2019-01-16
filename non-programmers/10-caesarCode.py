import string
from collections import deque

print("""
# Get text to encode
# Get key for caesar cipher
# Encode text using caesar cipher with key
# Decode encoded text
""")

try:
    text2Encode = input("Please write the text you wish to encode:")
except ValueError:
    print("This is not a text, go fuck yourself!!!")

try:
    cipherKey = input("Please write the cipher letter:")
except ValueError:
    print("This is not a valid key, go fuck yourself!!!")

a2z = list(string.ascii_lowercase)
a2zShifted = a2z[len(a2z)-(a2z.index(cipherKey)+1):]+a2z[:len(a2z)-(a2z.index(cipherKey)+1)]

encodedText = [a2z[a2zShifted.index(x)] for x in list(text2Encode.lower())]
decodedText = [a2zShifted[a2z.index(x)] for x in encodedText]

print(list(text2Encode.lower()), encodedText, decodedText, sep="\n")
