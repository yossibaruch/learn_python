name = 'Zed A. Shaw'
age = 35 # not a lie
iheight = 74 # inches, 1 inch = 2.54 cm
lweight = 180 # lbs, 1 lbs = 0.4535923699997481 kg
i2c = 2.54
l2k = 0.4535923699997481
height = i2c * iheight
weight = l2k * lweight
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
#print "He's %d inches tall." % height
print "He's %d cm tall." % height
#print "He's %d pounds heavy." % weight
print "He's %d kilograms heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
