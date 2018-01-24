def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have", cheese_count, "cheeses!")
    print("You have", boxes_of_crackers, "boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def creating_an_ass_of_myself(number, power, shitty_text):
    print("your shitty text is:", shitty_text, "and you wanted to know:", number, "^", power, "=", number**power)


creating_an_ass_of_myself(2,3,"shit")
creating_an_ass_of_myself(amount_of_cheese,3,"shit")