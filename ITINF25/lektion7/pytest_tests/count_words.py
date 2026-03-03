# 10: Red - Skriv ett test som inte lyckas... ännu
# 20: Green - Få alla test hittils att passera, uppmuntrat att fuska
# 30: Refactor - Snygga till koden vid behov, inget mer test ska uppfyllas men alla ska fortsätta att passera
# 40: GOTO 10


def count_words(text_string):
    words = text_string.split()
    count = dict()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count
