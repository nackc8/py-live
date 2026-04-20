# 1337  Elite!
# haxor Utvecklare

# fmt: off
computer_words = {
    "1337": "Elite!",
    "haxor": "Utvecklare"
}
# fmt: on

p = print

for key_value in computer_words.items():
    p(key_value[0])
    p(key_value[1])
    p("---")
