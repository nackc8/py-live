import argparse
import sys
from pathlib import Path

# Se am1.py för vad vi översätter till argparse

parser = argparse.ArgumentParser(
    description="What the program does",
    epilog="Text at the bottom of help",
)

#        -c, -C, --complement
#               use the complement of ARRAY1
#        -d, --delete
#               delete characters in ARRAY1, do not translate


parser.add_argument(
    "-c",
    "-C",
    "--complement",
    action="store_true",
    help="use the complement of STRING1",
)

parser.add_argument(
    "-d",
    "--delete",
    action="store_true",
    help="delete characters in STRING1, do not translate",
)


parser.add_argument("filename", metavar="FILENAME", help="the file to process")
parser.add_argument("string1", metavar="STRING1")
parser.add_argument("string2", metavar="STRING2", nargs="?")

parsed_args = parser.parse_args(sys.argv[1:])

if parsed_args.delete and parsed_args.string2:
    parser.error("argument --delete: expected one string")
elif not parsed_args.delete and not parsed_args.string2:
    parser.error("expected 2 arguments")

filename = Path(parsed_args.filename)

if not filename.exists():
    parser.error(f"missing file {filename}")

# Allt är bra! Dags att jobba!


def delete_operation(row):
    """Returnerar rad med alla tecken i string1 borttagna"""
    output_row = ""
    for character in row:
        matched_character = character in parsed_args.string1
        skip = (
            matched_character if not parsed_args.complement else not matched_character
        )
        if skip:
            continue
        output_row += character

    return output_row


def substitute_operation(row):
    output_row = ""
    for character in row:
        for index, match_character in enumerate(parsed_args.string1):
            replace_character = (
                parsed_args.string2[index]
                if len(parsed_args.string1) == len(parsed_args.string2)
                else parsed_args.string2[-1]
            )
            

            # print(
            #     f"index: {index} match_character: {match_character} replace_character: {replace_character}"
            # )
        # break  # Tillfälligt

    return output_row


output = ""
# open har stöd för att användas som "context"
with open(filename, "r") as twrap:
    for rad in twrap.readlines():
        if parsed_args.delete:
            output += delete_operation(rad)
        else:
            output += substitute_operation(rad)


print("Slut", output, sep="\n")
