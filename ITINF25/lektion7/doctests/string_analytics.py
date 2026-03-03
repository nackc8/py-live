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

    It can also count five "hopp":

    >>> count_words("hopp hopp hopp hopp hopp")
    {"hopp": 5}

    It cannot cound three "hopp" wrong:

    >>> count_words("hopp hopp hopp") != {"hopp": 2}
    True

    Do not use it with ints:

                count_words(12345)



    """
    words = text_string.split()
    count = dict()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count
