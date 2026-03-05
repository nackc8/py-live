import sys

# Lets mimic the tr command:
#        NAME
#          tr - translate or delete characters
#
#        ...
#
#        SYNOPSIS
#        tr [OPTION]... STRING1 [STRING2]
#        -c, -C, --complement
#               use the complement of ARRAY1
#        -d, --delete
#               delete characters in ARRAY1, do not translate


class InvalidInputError(ValueError):
    pass


try:
    option_complement = False
    option_delete = False
    all_args = sys.argv[1:]
    for arg in enumerate(all_args):
        print("arg: ", arg)
        if arg == "-c" or arg == "-C" or arg == "--complement":
            if option_complement:
                raise InvalidInputError("Only specify complement once!")
            option_complement = True
        elif arg == "-d" or arg == "--delete":
            if option_delete:
                raise InvalidInputError("Only specify delete once!")
            option_delete = True
        else:
            break
    print("loop is breaked!")
except InvalidInputError as e:
    print("Call error: ", str(e), file=sys.stderr)
    sys.exit(1)
