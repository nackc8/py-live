#!/usr/bin/env python3

import sys


def studder(msg):
    output = ""

    # enumerate("hej") -> [(0,"h"),(1,"e"), (2, "j")]

    # index, char är "unboxing" vilket tar positionerna
    # i tupeln och tilldelar dem till variablerna - i den
    # ordning de skrivs.
    for index, char in enumerate(msg):
        if index % 2 == 0:
            output = output + char

    return output


print("(remove this line in prod) My name is:", __name__)

# Vid import: __name__ == "studder"
if __name__ == "__main__":
    # 2 för att skriptets eget namn är först
    if len(sys.argv) != 2:
        print("Usage: studder.py MSG", file=sys.stderr)
        sys.exit(1)
    print(studder(sys.argv[1]))
