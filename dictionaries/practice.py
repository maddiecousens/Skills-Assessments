"""Dictionaries Practice

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""
from collections import defaultdict, Counter

def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """

    ## Using Dictionaries: ##

    # unique_words = {}

    # for word in words:
    #     unique_words[word] = unique_words.get(word, 0) + 1

    # return sorted(unique_words.keys())

    # Using Sets
    return list(set(words))


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """

    # using sets: 
    return list(set(items1) & set(items2))
    # # Using Dictionaries:
    # unique_words1 = {}
    # unique_words2 = {}

    # for word in items1:
    #     unique_words1[word] = unique_words1.get(word, 0) + 1

    # for word in items2:
    #     unique_words2[word] = unique_words2.get(word, 0) + 1

    # word_set = []

    # for key in unique_words1.keys():
    #     for key2 in unique_words2.keys():
    #         if key == key2:
    #             word_set.append(key)

    # return word_set



def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """

    #### Using Only Dictionaries: ####

    # pairs_dict = {}

    # # Account for case when 0 is included
    # if 0 in numbers:
    #     pairs_dict[(0, 0)] = True

    # # Iterate over range of list
    # for i in xrange(len(numbers) - 1):
            
    #     # starting at index i, iterate over rest of numbers in list, beginning
    #     # at i+1 because a number added itself will not be zero, unless it is
    #     # 0 which is already accounted for on line 124
    #     for j in xrange(1, len(numbers) - i):
            
    #         num1 = numbers[i]
    #         num2 = numbers[i + j]
            
    #         # If the {num1, num2} not in dict already and num1 + num2 == 0, add to
    #             # to dictionary
    #         if (((num1, num2) and (num2, num1)) not in pairs_dict) and (num1 + num2) == 0:
    #             pairs_dict[(num1, num2)] = True

    # return [list(key) for key in pairs_dict.keys()]

    ### Using list comprehension

    return [[num, -num] for num in set(numbers) if -num in set(numbers) and num >= 0]




def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    cnt = Counter(phrase.replace(' ',''))
    most = [cnt.most_common()[0][0]]
    high = cnt.most_common()[0][1]


    for item in cnt.most_common()[1:]:

        if item[1] == high:
            most.append(item[0])
    return most


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
