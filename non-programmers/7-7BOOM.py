print("""
# Ask user for integer
# Get user input
# print number from 1 to n,
# Substitute numbers divised by 7 or contain 7 as a digit with 'BOOM!'
""")

N = int(input("Please give me N so we can play 7BOOM: "))

for i in range(N):
    if "7" in str(i) or i % 7 == 0:
        print("BOOM!")
    else:
        print(str(i))
