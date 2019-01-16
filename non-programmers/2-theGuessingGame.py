import random

print("""
# Please pick a number to be guessed
# Then we ask the user to guess a number
# get the number guessed
# response with right / wrong and iterate
""")

number = random.randint(1, 100)

while 1 == 1:
    guessed = int(input("number: "))
    print("Correct!!!" if number == guessed else "wrong! Guess again... HINT: ")
    exit(0) if number == guessed else print(">" if number > guessed else "<")

