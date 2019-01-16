print("""
# Ask user for number
# Add this number to sum
# Repeat two steps until user inserts nothing
# Print sum
""")

print("""
Please write down numbers, press enter after each one. enter Blank for calculation of sum...
(numbers must be integers...)
""")

listForSum = []
while True:
    added = input("sum+= ")
    if added == "":
        print(sum(listForSum), "is the sum of floats entered, thank you!!!")
        exit(0)
    try:
        added = float(added)
    except ValueError:
        print("Not a FLOAT!!!")
        continue
    listForSum.append(added)
