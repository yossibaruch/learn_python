import ex25


def break_words(stuff):
    """This function will break up words for us."""
    return stuff.split(' ')


def sort_words(wordss):
    """Sorts the words."""
    return sorted(wordss)


def print_first_word(wordss):
    """Prints the first word after popping it off."""
    print(wordss.pop(0))


def print_last_word(wordss):
    """Prints the last word after popping it off."""
    print(wordss.pop(-1))


def sort_sentence(sentencess):
    """Takes in a full sentence and returns the sorted words."""
    return sort_words(break_words(sentencess))


def print_first_and_last(sentencess):
    """Prints the first and last words of the sentence."""
    print_first_word(break_words(sentencess))
    print_last_word(break_words(sentencess))


def print_first_and_last_sorted(sentencess):
    """Sorts the words then prints the first and last one."""
    print_first_word(sort_sentence(sentencess))
    print_last_word(sort_sentence(sentencess))


print("Let's practice everything.")
print("You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 6
print("This should be five: %s" % five)


def secret_formula(started):
    jelly_beanss = started * 500
    jarss = jelly_beanss / 1000
    cratess = jarss / 100
    return jelly_beanss, jarss, cratess


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: %d" % start_point)
print("We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crates." % (secret_formula(start_point)))

sentence = "All god\tthings come to those who weight."

words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
print(sorted_words)

print_first_and_last(sentence)
print_first_and_last_sorted(sentence)
