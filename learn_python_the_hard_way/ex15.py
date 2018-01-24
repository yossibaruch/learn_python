from sys import argv
script, filename = argv
txt = open(filename)
print("here is your file:", filename)
print(txt.read())

print("Print the filename again:")
file_again = input("> ")

txt_again = open(file_again)
print(txt_again.read())
txt.close()
txt_again.close(