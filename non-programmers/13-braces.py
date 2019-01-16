import string

print("""
# Iterate on characters from string
    # Find opening braces and "remember" them in order
    # Find closing braces and make sure it fits the last opening braces
        # If "yes", forget last opening braces
        # If "no", return False
# If memory of opening braces is not empty - return False
# else return True
""")


def hebrew_braces(braces_list):
    braces_work = []
    for c in braces_list:
        if c in '{[(':
            braces_work.append(c)
        if c in '}])':
            try:
                b = braces_work.pop()
            except IndexError:
                return False
            if (b == '(' and c == ')') or (b == '[' and c == ']') or (b == '{' and c == '}'):
                continue
            else:
                print("Not balanced braces")
                return False
    print("Balanced braces")
    return True


while True:
    try:
        bracesWithChars = str(input("Please enter a string with braces:"))
    except ValueError:
        print("This value is erroneous, please mend")
        continue
    break

whatToRemove = string.printable
for bra in ['{', '}', '[', ']', '(', ')']:
    whatToRemove = whatToRemove.replace(bra, '')

bracesOnly = bracesWithChars
for let in list(whatToRemove):
    bracesOnly = bracesOnly.replace(str(let), '')

# print(bracesWithChars, bracesOnly, whatToRemove)

bracesOnly = list(bracesOnly)
print(bracesOnly)

hebrew_braces(bracesOnly)
