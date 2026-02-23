# **replacements = tar alla nyckelordsargument
def template(content, **replacements):
    # Överkurs just nu! Återkom senare.
    for key, value in replacements.items():
        x = content.replace(key, value)
        print(x)


template("nackademin gurka", nack="hopp", gurka="grön")
