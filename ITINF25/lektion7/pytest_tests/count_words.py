# 10: Red - Skriv ett test som inte lyckas... ännu
# 20: Green - Få alla test hittils att passera, uppmuntrat att fuska
# 30: Refactor - Snygga till koden vid behov, inget mer test ska uppfyllas men alla ska fortsätta att passera
# 40: GOTO 10


def count_words(text_string):
    lst = text_string.split()

    if text_string == "hej hej hej hej hej hej hej hej hej hej":
        return {"hej": 10}
    elif text_string == "hej hej hej hopp hopp hopp":
        return {"hej": 3, "hopp": 3}
    else:
        return {"hopp": 5}
