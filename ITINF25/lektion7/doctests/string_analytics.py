"""
Different functions to analyse strings
"""


def count_words(text_string):
    """
    Counts occurances of words in a string and returns a
    dictionary with word -> occurance key values.

    It can for example count ten "hej"

    >>> count_words("hej hej hej hej hej hej hej hej hej hej")
    {"hej": 10}

    """
    words = text_string.split()
    count = dict()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count
