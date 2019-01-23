print("""
# Get a word to be guessed, and then hide it
# While user has more guesses:
#   - Ask for user to guess a letter or entire word,
#     - Show word guessed until now and show him number of guesses left
#   - If letter - reveal letters in word
#   - If word
#     - If wrong - notify
#     - If correct - notify and end game
#   - Reduce number of guesses
#   - If no more guesses - notify and end game
""")

while True:
    try:
        word = input("Please write down the word you want me to guess:")
    except ValueError:
        print("Wrong value, retry...")
        continue
    if " " in word:
        print("Should be a single word")
        continue
    break

wordList = list(word)
wordComplete = [""]*len(wordList)

for i in range(round(len(word)*1.5)):
    print(wordComplete)
    if wordComplete == wordList:
        print("Word is:", word, " and you guessed correctly")
        exit(0)
    guess = input("Guess: ")
    if guess in word:
        for j in [i for i, x in enumerate(wordList) if x == guess]:
            wordComplete[j] = guess
        print(guess, " is in word")
        # print(word, wordList, wordComplete)
    else:
        print(guess, " is not in word...")

print("Word is:", word, " and you failed to guess it!!!!")
