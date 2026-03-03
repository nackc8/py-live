"""
Counts occurances of words in a string and returns a
dictionary with word -> occurance key values.
"""


def count_words(text_string):
    words = text_string.split()
    count = dict()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count
