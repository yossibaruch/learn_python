from sys import argv

script, user_name = argv
prompt = '> '

print("Hi", user_name, "I'm the ", script, "script")
print("I'd like to ask you a few questions.")
print("Do you like me", user_name, "?")
likes = input(prompt)

print("Where do you live", user_name, "?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("Alright, so you said", likes,
      "about liking me.\nYou live in", lives,
      "Not sure where that is.\nAnd you have a", computer,
      "computer.  Nice.")
