def break_words(stuff):
    """This function will break up words for us."""
    return stuff.split(' ')


def sort_words(words):
    """Sorts the words"""
    return sorted(words)


def print_first_word(words):
    """prints the first word after popping it off."""
    print(words.pop(0))


def print_last_word(words):
    """prints the last word after popping it off."""
    print(words.pop(-1))


def sort_sentence(sentence):
    """Takes in full sentence and returns the sorted words."""
    return sort_words(break_words(sentence))


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    print_first_word(break_words(sentence))
    print_last_word(break_words(sentence))


def print_first_and_last_sorted(sentence):
    """Prints the first and last words of the sentence."""
    print_first_word(sort_sentence(sentence))
    print_last_word(sort_sentence(sentence))

    