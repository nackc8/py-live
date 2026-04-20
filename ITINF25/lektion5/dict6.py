# 1337  Elite!
# haxor Utvecklare

# fmt: off
computer_words = {
    "1337": "Elite!",
    "haxor": "Utvecklare"
}
# fmt: on

p = print

# Med unpacking för läsbarhet
for key, value in computer_words.items():
    p(key)
    p(value)
    p("---")
