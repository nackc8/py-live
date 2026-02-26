def screamtext(text):
    return text.upper()


def fancytext(text):
    # list comprehension, med en ternary if som avgör om en bokstav ska
    # vara versal eller inte
    text = [
        character if index % 2 == 0 else character.upper()
        for index, character in enumerate(text)
    ]
    text = "".join(text)
    return text
