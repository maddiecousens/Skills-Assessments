"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""

from collections import defaultdict, Counter

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    #### There are many ways to do this: ####

    # 1) Using built in .get method

    # words = phrase.split()
    # unique_words = {}

    # for word in words:
    #     unique_words[word] = unique_words.get(word, 0) + 1

    # return unique_words

    #########################################
    # 2) Using .setdefault method

    # words = phrase.split()
    # unique_words = {}

    # for word in words:
    #     unique_words[word] = unique_words.setdefault(word, 0) + 1

    # return unique_words

    #########################################

    # 3) Using defaultdicts

    # words = phrase.split()

    # unique_words = defaultdict(int)

    # for word in words:
    #     unique_words[word] += 1

    # return unique_words

    #########################################

    # 4) Using the Counter class
    
    # Create list of words using the string split method
    words = phrase.split()

    # The Counter class returns a dictionary of counts over an iterterable. In
        # this case the iterable is a list of words
    return Counter(words)

def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """
    # Create dictionary of melon prices
    melon_dict = {"Watermelon": 2.95,
                  "Cantaloupe": 2.50,
                  "Musk": 3.25,
                  "Christmas": 14.25}
    # First way:
    # Check whether melon name is a key in melon dictionary and return price
        # of melon. Otherwise return 'No price found'
    # if melon_name in melon_dict:
    #     return melon_dict[melon_name]
    # else:
    #     return 'No price found'
    return melon_dict.get(melon_name, 'No price found')


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """
    # Create a default dictionary
    word_length = defaultdict(list)

    # Iterate over words in sorted word list
    for word in sorted(words):
        # Add length of word as key to dictionary and append word to value list
        word_length[len(word)].append(word)

    # return sorted dictionary items
    return sorted(word_length.items())


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    # create dicitonary of english to pirate
    eng_to_pirate = {"sir": "matey",
                     "hotel": "fleabag inn",
                     "student": "swabbie",
                     "man": "matey",
                     "professor": "foul blaggart",
                     "restaurant":"galley",
                     "your": "yer",
                     "excuse": "arr",
                     "students": "swabbies",
                     "are": "be",
                     "restroom": "head",
                     "my": "me",
                     "is": "be"}

    phrase_words = phrase.split()

    #creating new list because it's not good practice to adjust a list
        #while iterating over it. However, I wanted to change list in place
        # I would us enumerate, and if the word was in the dictionary, change
        # the word at that index.
    translated_phrase = []

    for word in phrase_words:
        # if word is in the dictionary, translate word and append to final list
        if word in eng_to_pirate:
            word = eng_to_pirate[word]
            translated_phrase.append(word)
        #otherwise append word as is to final list
        else:
            translated_phrase.append(word)


    return " ".join(translated_phrase)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Another example:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    # Initialize a dictionary with default list values
    game_dict = defaultdict(list)

    # Create an output string of words, initialzed with first name in game
    first_name = names[0]
    game_output = [first_name]

    # Create variable that is the last letter of the word, initialized for first
        # word
    last_letter = first_name[-1]

    # Create a dictionary where keys are the first letters in words and the
        # values are a list of all names that begin with that letter, in order
        # of appearance.

    for name in names[1:]:
        game_dict[name[0]].append(name)
    
    # While there is a key that correspands to the last letter in the name,
        # and there is another name that begins with that letter, complete the
        # content of the while loop.
    while game_dict.setdefault(last_letter, False) and game_dict[last_letter][0]:
            # Look up the last letter in dictionary and use pop to retrieve and 
                # remove the first name in value list
            new_name = game_dict[last_letter].pop(0)

            # Append new name to game output
            game_output.append(new_name)

            # Reset the last_letter variable to the last letter of new name
            last_letter = new_name[-1]

    return game_output

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
